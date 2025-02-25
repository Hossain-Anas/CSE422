import heapq

graph = {}
heuristic = {}

def create_graph(file):

    with open(file, "r") as inp_file:
        for line in inp_file:
            l = line.split()
            curr_node = l[0]
            heuristic_val = int(l[1])
            adj_nodes = {}

            for i in range(2, len(l), 2):
                node = l[i]
                weight = int(l[i+1])
                adj_nodes[node] = weight

            
            heuristic[curr_node] = heuristic_val
            graph[curr_node] = adj_nodes

def a_star(start, goal):
    pq = [(heuristic[start], start, [start], 0)]
    visited = set()

    while pq:

        fn, curr_node, path, weight = heapq.heappop(pq)

        if curr_node == goal:
            return path, weight
        
        if curr_node in visited:
            continue
        
        visited.add(curr_node)

        for u,w in graph[curr_node].items():

            if u in visited:
                continue

            w_update = weight + w
            fn_update = w_update + heuristic[u]

            new_path = path + [u]
            heapq.heappush(pq, (fn_update, u, new_path, w_update))

        
    return None, None



create_graph("Input file.txt")

start = input("Start node: ")
goal = input("Destination: ")


path, weight = a_star(start, goal)

if path or weight is not None:
    print(f"Path : {'->'.join(path)}")
    print(f"Total Distance: {weight}")

else:
    print("NO PATH FOUND")


# print(graph)
