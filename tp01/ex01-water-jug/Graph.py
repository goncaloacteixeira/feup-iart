class Node:
    parent = None

    def __init__(self, initial, final, description):
        self.initial = initial
        self.final = final
        self.description = description

    def __eq__(self, o) -> bool:
        return o.final == self.final

    def __hash__(self) -> int:
        return self.initial[0] * 13 + self.initial[1] * 17 - self.final[0] * 13 - 1 + self.final[1] * 7

    def print(self):
        print(self.initial, " - ", self.description, " - ", self.final)


def print_solution(path: list):
    [x.print() for x in path]


class Graph:
    levels = []

    def add_level(self):
        self.levels.append([])

    def add_node(self, node: Node, level: int):
        self.levels[level - 1].append(node)

    def find_goals_depth(self, goal: tuple, depth: int) -> list:
        solutions = []
        for state in self.levels[depth - 1]:
            if state.final == goal:
                solutions.append(state)
        return solutions

    def path(self, destination: Node):
        node = destination
        path = [destination]
        while node != self.levels[0][0]:
            path.append(node.parent)
            node = node.parent
        path.reverse()
        return path
