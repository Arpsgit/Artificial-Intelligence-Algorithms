def bfsearch(tree:dict, start_state: str, goal_state:str) -> list: 
    parent = {} # to track the parent of a node
    #visited = []
    node_queue = [start_state] # as we know that bfs uses queue structure to expand its child node, level by level.
    while node_queue:
        if node_queue[0] == goal_state:
            node = node_queue[0]
            path = [node]
            while node != start_state:
                node = parent[node]
                path.append(node)
            path.reverse()
            return path
        else:
            if node_queue[0] in tree.keys():
                for child in tree[node_queue[0]]:
                    parent[child] = node_queue[0] 
                    node_queue.append(child)
                #visited.append(node_queue[0])
                node_queue.pop(0)
            else:
                #visited.append(node_queue[0])
                node_queue.pop(0)

def print_path(path:list): # for printing the shortest path from start node to goal node
    print(path[0], end = " ")
    for i in range(1,len(path)):
        print("->", path[i], end = " ")

if __name__ == '__main__':
    tree = {'a':['b','c','d'], 'b':['e','f'], 'c':['g','h']} # A demo tree
    p = bfsearch(tree,'a','h')
    print_path(p)

# Output: a -> c -> h 
