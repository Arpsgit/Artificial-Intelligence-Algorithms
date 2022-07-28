def dfs(graph: dict, start_node: str, goal_node: str)-> list:
    parent = {} # for tracking the parent of the nodes
    node_stack = [] # for expand the nodes one by one in lifo order
    visited = [] # for tracking the visited nodes
    visited.append(start_node)
    node_stack.append(start_node)
    while node_stack:
        node = node_stack[0]
        if node == goal_node:
            path = [node]
            while node != start_node:
                node = parent[node]
                path.append(node)
            path.reverse()
            return path
        else:
            if node in graph.keys():
                node_stack.pop(0)
                for child in graph[node]:
                    if child not in visited:
                        parent[child] = node
                        node_stack.insert(0, child)
                        visited.append(child)
            else:
                node_stack.pop(0)

def print_path(path: list):
    print(path[0], end = " ")
    for i in range(1,len(path)):
        print("->", path[i], end = " ")

if __name__ == '__main__':
    # A demo graph. Here Start node is s and goal node is g.
    adj_list = {'s':['a','d'], 'a':['s','d','b'], 'd':['s','a','e'], 'b':['a','e','c'], 'e':['d','b','f'], 'c':['b'], 'f':['e','g'], 'g':['f']}

    print_path(dfs(adj_list, 's', 'g'))