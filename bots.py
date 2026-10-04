from routing import RouteEngine

class NavigationAgent:
    def __init__(self, title, search_type, campus):
        self.title = title
        self.search_type = search_type
        self.engine = RouteEngine(campus)

    def route(self, start, finish):
        return self.engine.search(start, finish, self.search_type)

class Pathfinder(NavigationAgent):
    def __init__(self, campus):
        super().__init__("PATHFINDER", "greedy", campus)

class Orbit(NavigationAgent):
    def __init__(self, campus):
        super().__init__("ORBIT", "astar", campus)
