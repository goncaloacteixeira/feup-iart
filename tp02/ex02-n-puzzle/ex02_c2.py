from State import *
from Utils import *
import time


def aStar(state: State, N: int):
    root = Node(state)
    stack = [root]
    tree = Tree(root)

    root.heuristics = h1(state.board) + h2(state.board)

    visited = []
    # keeping track of current tree depth
    depth = 1
    while depth != 1000 and len(stack) != 0:
        stack.sort(key=lambda x: x.heuristics)

        s = stack.pop(0)
        depth = s.depth
        # print("visited:", len(visited), "stack:", len(stack), "depth:", depth, "h:", s.heuristics)

        if flatten(s.info.board) not in visited:
            expanded = expand(s.info, N)
            # for each descendant we add the node to the tree and the new stack
            # we also create an edge between the parent and the newly created node
            for x in expanded:
                new_node = Node(x)
                new_node.heuristics = s.heuristics + h2(x.board) + h1(x.board)
                stack.append(new_node)
                tree.add_node(new_node)
                s.add_edge(new_node, 1)
            # as we already expanded 's' we need to add it's final state to the visited list
            visited.append(flatten(s.info.board))

        solution = contains_goal(stack, N)
        if solution is not None:
            print("Found Solution, Depth", depth)
            return solution, tree

    # just to return if max depth is reached, as we dont want to keep an infinite loop,
    # the solution may be on depth 10000, as this is BFS we have no way to guarantee a
    # solution is found, so we keep a maximum depth expansion
    return None, tree


if __name__ == "__main__":
    print("---- A* -----")

    print("8-PUZZLE")
    board = [
        [1, 2, 3],
        [5, 0, 6],
        [4, 7, 8]
    ]
    initial = State(board, (1, 1), "Start")
    print(initial)

    t = time.time_ns()
    node, tree = aStar(initial, 8)
    if node is not None:
        path = find_path(node)
        print("- Solution -")
        print_path(path)
    else:
        print("- No Solution -")
    elapsed_time = time.time_ns() - t
    print("Elapsed Time:", elapsed_time / 1000.0, "ms")

    print("8-PUZZLE")
    board = [
        [1, 3, 6],
        [5, 2, 0],
        [4, 7, 8]
    ]
    initial = State(board, (2, 1), "Start")
    print(initial)

    t = time.time_ns()
    node, tree = aStar(initial, 8)
    if node is not None:
        path = find_path(node)
        print("- Solution -")
        print_path(path)
    else:
        print("- No Solution -")
    elapsed_time = time.time_ns() - t
    print("Elapsed Time:", elapsed_time / 1000.0, "ms")

    print("8-PUZZLE")
    board = [
        [1, 6, 2],
        [5, 7, 3],
        [0, 4, 8]
    ]
    initial = State(board, (0, 2), "Start")
    print(initial)

    t = time.time_ns()
    node, tree = aStar(initial, 8)
    if node is not None:
        path = find_path(node)
        print("- Solution -")
        print_path(path)
    else:
        print("- No Solution -")
    elapsed_time = time.time_ns() - t
    print("Elapsed Time:", elapsed_time / 1000.0, "ms")

    print("16-PUZZLE")
    board = [
        [5, 1, 3, 4],
        [2, 0, 7, 8],
        [10, 6, 11, 12],
        [9, 13, 14, 15]
    ]
    initial = State(board, (1, 1), "Start")
    print(initial)

    t = time.time_ns()
    node, tree = aStar(initial, 15)
    if node is not None:
        path = find_path(node)
        print("- Solution -")
        print_path(path)
    else:
        print("- No Solution -")
    elapsed_time = time.time_ns() - t
    print("Elapsed Time:", elapsed_time / 1000.0, "ms")
