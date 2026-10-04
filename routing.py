import heapq
import itertools
import time
from dataclasses import dataclass

@dataclass
class RouteResult:
    path: list
    cost: float
    explored: int
    seconds: float

class RouteEngine:
    def __init__(self, campus):
        self.campus = campus

    def search(self, start, goal, algorithm):
        if start not in self.campus.places or goal not in self.campus.places:
            raise ValueError("Location is not listed in campus.json")
        if start == goal:
            return RouteResult([start], 0, 0, 0.0)

        began = time.perf_counter()
        serial = itertools.count()
        state = (start, self.campus.start_mode(start))
        initial_h = self.campus.estimate(start, goal)
        frontier = [(self.priority(0, initial_h, algorithm), next(serial),
                     0, state, [start])]
        known = {state: 0}
        explored = 0

        while frontier:
            _, _, spent, current_state, path = heapq.heappop(frontier)
            place, mode = current_state
            if spent != known.get(current_state):
                continue
            explored += 1
            if place == goal:
                return RouteResult(path, spent, explored, time.perf_counter() - began)

            for neighbour, weight, next_mode in self.campus.legal_moves(place, mode, goal):
                new_cost = spent + weight
                next_state = (neighbour, next_mode)
                if new_cost >= known.get(next_state, float("inf")):
                    continue
                known[next_state] = new_cost
                estimate = self.campus.estimate(neighbour, goal)
                rank = self.priority(new_cost, estimate, algorithm)
                heapq.heappush(frontier, (rank, next(serial), new_cost,
                                          next_state, path + [neighbour]))

        return RouteResult([], float("inf"), explored, time.perf_counter() - began)

    @staticmethod
    def priority(cost_so_far, estimate, algorithm):
        return estimate if algorithm == "greedy" else cost_so_far + estimate
