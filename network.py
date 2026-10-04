import heapq
import json

class CampusNetwork:
    def __init__(self, filename="campus.json"):
        with open(filename, encoding="utf-8") as stream:
            data = json.load(stream)
        self.places = tuple(data["locations"])
        self.links = {place: {} for place in self.places}
        for first, second, metres in data["edges"]:
            self.links[first][second] = metres
            self.links[second][first] = metres
        self.cse = {"CSE Laboratory", "CSE_AKC Seminar Hall", "CSE_Reflxon Room"}
        self.gates = {"Tower 2 Front Entry", "Tower 2 Rear Entry"}

    def adjacent(self, place):
        return self.links[place].items()

    def estimate(self, start, goal):
        costs = {place: float("inf") for place in self.places}
        costs[goal] = 0
        queue = [(0, goal)]
        while queue:
            total, place = heapq.heappop(queue)
            if total != costs[place]:
                continue
            if place == start:
                return total
            for neighbour, metres in self.adjacent(place):
                candidate = total + metres
                if candidate < costs[neighbour]:
                    costs[neighbour] = candidate
                    heapq.heappush(queue, (candidate, neighbour))
        return costs[start]

    def start_mode(self, place):
        return "inside" if place in self.cse else "outside"

    def legal_moves(self, place, mode, goal):
        for neighbour, metres in self.adjacent(place):
            if goal in self.cse:
                if mode == "outside":
                    if place in self.gates and neighbour == "Lift Area":
                        yield neighbour, metres, "entry"
                    elif place == "Lift Area" and neighbour in self.cse:
                        yield neighbour, metres, "inside"
                    elif neighbour not in self.cse and neighbour != "Lift Area":
                        yield neighbour, metres, "outside"
                elif mode == "entry":
                    if place == "Lift Area" and neighbour in self.cse:
                        yield neighbour, metres, "inside"
                elif mode == "inside":
                    if neighbour in self.cse:
                        yield neighbour, metres, "inside"
                    elif neighbour == "Lift Area":
                        yield neighbour, metres, "exit"
                elif mode == "exit" and neighbour in self.gates:
                    yield neighbour, metres, "outside"
            else:
                if mode == "outside":
                    if neighbour not in self.cse and not (
                        place in self.gates and neighbour == "Lift Area"
                    ):
                        yield neighbour, metres, "outside"
                elif mode == "inside":
                    if neighbour in self.cse:
                        yield neighbour, metres, "inside"
                    elif neighbour == "Lift Area":
                        yield neighbour, metres, "exit"
                elif mode == "exit" and neighbour in self.gates:
                    yield neighbour, metres, "outside"
