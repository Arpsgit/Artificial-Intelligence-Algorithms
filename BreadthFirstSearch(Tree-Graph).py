def bfs(graph : dict, start_node : str, goal_node : str)->list:
    parent = {} # for tracking the parent of the nodes
    node_queue = [] # for expand the nodes one by one in fifo order
    visited = [] # for tracking the visited nodes
    visited.append(start_node)
    node_queue.append(start_node)
    while node_queue:
        if node_queue[0] == goal_node:
            node = node_queue[0]
            path = [node]
            while node != start_node:
                node = parent[node]
                path.append(node)
            path.reverse()
            return path
        else:
            if node_queue[0] in graph.keys():
                for child in graph[node_queue[0]]:
                    if child not in visited:
                        parent[child] = node_queue[0] 
                        node_queue.append(child)
                        visited.append(child)
                node_queue.pop(0)
            else:
                node_queue.pop(0)

def print_path(path: list):
    print(path[0], end = " ")
    for i in range(1,len(path)):
        print("->", path[i], end = " ")

if __name__ == '__main__':
    # A demo graph. Here Start node is s and goal node is g.
    adj_list = {'s':['a','d'], 'a':['s','d','b'], 'd':['s','a','e'], 'b':['a','e','c'], 'e':['d','b','f'], 'c':['b'], 'f':['e','g'], 'g':['f']}

    print_path(bfs(adj_list, 's', 'g'))