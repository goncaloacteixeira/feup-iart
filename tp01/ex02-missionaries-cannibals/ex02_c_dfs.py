from State import *
from Utils import *


# Depth First Search - pesquisa em profundidade
def dfs(state: State, goal: tuple = (0, 0, -1), max_depth: int = 15):
    root = Node(state)
    stack = [root]
    tree = Tree(root)

    # list containing states (x,y) which were already discovered (this is an improvement)
    visited = []
    # if the stack is empty we also want to terminate the loop as no more nodes are expandable
    while len(stack) != 0:
        # popping the first node on the stack (current highest depth node)
        node = stack.pop(0)
        # adding the node to the visited list, we do this here so when we are expanding the nodes
        # we dont add to the stack nodes already discovered, including the parent
        visited.append(node.info.final)

        # here we expand said node
        expanded = expand(node.info)

        if node.depth != max_depth:
            # for each expanded node we want to add it to the tree, and insert it on the stack so on
            # the next loop we start by the highest depth nodes
            for x in expanded:
                if x.final not in visited:
                    new_node = Node(x)
                    tree.add_node(new_node)
                    node.add_edge(new_node, 1)
                    stack.insert(0, new_node)

        # The solution may not be optimal, but it's faster than the BFS method, and takes less space
        solution = contains_goal(stack, goal)

        if solution is not None:
            print("Found Solution, Depth", solution.depth)
            return solution, tree

    return None, tree


if __name__ == "__main__":
    print("---- DFS -----")
    node, tree = dfs(State((3, 3, 1), (3, 3, 1), "Start"))
    print("- Tree -")
    tree.print_tree()
    if node is not None:
        path = find_path(node)
        print("- Solution -")
        print_path(path)
    else:
        print("- No Solution -")
