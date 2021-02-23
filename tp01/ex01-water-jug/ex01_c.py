from Graph import *


def expand(_state: Node):
    (x, y) = _state.final

    expanded = []

    if x + y >= 4 and y > 0:
        if x != 4 or y != y - (4 - x):
            expanded.append(Node(_state.final, (4, y - (4 - x)),
                                 "Pour water from the 3L bucket to completely fill the 4L bucket"))
    if x + y >= 3 and x > 0:
        if x != x - (3 - y) or y != 3:
            expanded.append(Node(_state.final, (x - (3 - y), 3),
                                 "Pour water from the 4L bucket to completely fill the 3L bucket"))
    if x + y <= 4 and y > 0:
        if x != x + y or y != 0:
            expanded.append(Node(_state.final, (x + y, 0), "Pour all the water from the 3L bucket to the 4L bucket"))
    if x + y <= 3 and x > 0:
        if x != 0 or y != x + y:
            expanded.append(Node(_state.final, (0, x + y), "Pour all the water from the 4L bucket to the 3L bucket"))
    if x < 4:
        expanded.append(Node(_state.final, (4, y), "Fill the 4L bucket"))
    if y < 3:
        expanded.append(Node(_state.final, (x, 3), "Fill the 3L bucket"))
    if x > 0:
        expanded.append(Node(_state.final, (0, y), "Empty the 4L bucket"))
    if y > 0:
        expanded.append(Node(_state.final, (x, 0), "Empty the 3L bucket"))

    for state in expanded:
        state.parent = _state

    return expanded


def found_goal(states, goal):
    for state in states:
        if state.final[0] == goal:
            return True
    return False


def bfs(state: Node, max_depth: int = 1000, goal: int = 2, logs: bool = False):
    states = [state]

    graph = Graph()
    graph.add_level()
    graph.add_node(state, 1)

    for depth in range(1, max_depth + 1):
        if logs: print("Depth", depth)
        expanded_states = []
        for s in states:
            if logs: print("Expanded from", s.final, end=": ")
            aux = expand(s)
            for e in aux:
                if logs: print(e.final, end=" ")
                expanded_states.append(e)
            if logs: print()
        states = expanded_states

        graph.add_level()
        [graph.add_node(x, depth + 1) for x in states]

        if found_goal(states, goal):
            print("Found Goal. Depth:", depth + 1)
            return graph, depth + 1


if __name__ == "__main__":
    print("--- BFS ---")
    graph, depth = bfs(Node((0, 0), (0, 0), "start"))
    goals = []
    for i in range(0, 4):
        [goals.append(x) for x in graph.find_goals_depth((2, i), depth)]
    for goal in goals:
        print("For goal:", goal.final)
        path = graph.path(goal)
        print_solution(path)

