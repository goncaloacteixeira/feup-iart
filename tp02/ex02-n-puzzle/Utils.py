from Tree import *


def flatten(nested):
    return [item for sublist in nested for item in sublist]


def contains_goal(nodes: list, N):
    goal = [x for x in range(1, N + 1)]
    goal.append(0)

    for node in nodes:
        flat_board = flatten(node.info.board)
        if flat_board == goal:
            return node
    return None


def find_path(node: Node):
    path = [node]

    while node.parent is not None:
        path.append(node.parent)
        node = node.parent

    path.reverse()
    return path


def print_path(path: list):
    for node in path:
        print(node.info)
