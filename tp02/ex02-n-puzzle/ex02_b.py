from State import *
from Utils import *
import time


# Breath First Search - pesquisa em largura
def bfs(state: State, N: int):
    root = Node(state)
    stack = [root]
    tree = Tree(root)

    # list containing states (x,y) which were already discovered
    visited = []
    # keeping track of current tree depth
    depth = 1
    while depth != 100:
        print("visited:", len(visited))
        # new stack to be looped on next cycle
        new_stack = []
        for s in stack:
            # expand each node of the stack
            if flatten(s.info.board) not in visited:
                expanded = expand(s.info, N)
                # for each descendant we add the node to the tree and the new stack
                # we also create an edge between the parent and the newly created node
                for x in expanded:
                    new_node = Node(x)
                    new_stack.append(new_node)
                    tree.add_node(new_node)
                    s.add_edge(new_node, 1)
                # as we already expanded 's' we need to add it's final state to the visited list
                visited.append(flatten(s.info.board))

            solution = contains_goal(new_stack, N)
            if solution is not None:
                print("Found Solution, Depth", depth)
                return solution, tree

        stack = new_stack
        depth += 1

    # just to return if max depth is reached, as we dont want to keep an infinite loop,
    # the solution may be on depth 10000, as this is BFS we have no way to guarantee a
    # solution is found, so we keep a maximum depth expansion
    return None, tree


# this will take TOOOO long :)
if __name__ == "__main__":
    print("---- BFS -----")

    print("8-PUZZLE")
    board = [
        [8, 4, 6],
        [5, 0, 7],
        [2, 3, 1]
    ]
    initial = State(board, (1, 1), "Start")
    print(initial)
    t = time.process_time()
    node, tree = bfs(initial, 8)
    if node is not None:
        path = find_path(node)
        print("- Solution -")
        print_path(path)
    else:
        print("- No Solution -")
    elapsed_time = time.process_time() - t
    print("Elapsed Time:", elapsed_time)

    print("15-PUZZLE")
    board = [
        [15, 2, 1, 12],
        [8, 5, 6, 11],
        [4, 9, 10, 7],
        [3, 14, 13, 0]
    ]
    initial = State(board, (3, 3), "Start")
    print(initial)

    t = time.process_time()
    node, tree = bfs(initial, 15)
    if node is not None:
        path = find_path(node)
        print("- Solution -")
        print_path(path)
    else:
        print("- No Solution -")
    elapsed_time = time.process_time() - t
    print("Elapsed Time:", elapsed_time)
