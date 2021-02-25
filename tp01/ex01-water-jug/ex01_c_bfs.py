from State import *
from Utils import *


# Breath First Search - pesquisa em largura
def bfs(state: State, goal: int = 2):
    root = Node(state)
    stack = [root]
    tree = Tree(root)

    # list containing states (x,y) which were already discovered
    visited = []
    # keeping track of current tree depth
    depth = 1
    while depth != 100:
        # new stack to be looped on next cycle
        new_stack = []
        for s in stack:
            # expand each node of the stack
            if s.info.final not in visited:
                expanded = expand(s.info)
                # for each descendant we add the node to the tree and the new stack
                # we also create an edge between the parent and the newly created node
                for x in expanded:
                    new_node = Node(x)
                    new_stack.append(new_node)
                    tree.add_node(new_node)
                    s.add_edge(new_node, 1)
                # as we already expanded 's' we need to add it's final state to the visited list
                visited.append(s.info.final)

            solution = contains_goal(new_stack, goal)
            if solution is not None:
                print("Found Solution, Depth", depth)
                return solution, tree

        stack = new_stack
        depth += 1

    # just to return if max depth is reached, as we dont want to keep an infinite loop,
    # the solution may be on depth 10000, as this is BFS we have no way to guarantee a
    # solution is found, so we keep a maximum depth expansion
    return None, tree


if __name__ == "__main__":
    print("---- BFS -----")
    node, tree = bfs(State((0, 0), (0, 0), "Start"), goal=2)
    print("- Tree -")
    tree.print_tree()
    if node is not None:
        path = find_path(node)
        print("- Solution -")
        print_path(path)
    else:
        print("- No Solution -")
