from Tree import *


def contains_goal(nodes: list, goal: int):
    for node in nodes:
        if node.info.final[0] == goal:
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
