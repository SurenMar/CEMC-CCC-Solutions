# https://cemc.uwaterloo.ca/sites/default/files/documents/2024/2024CCCSrProblems.html

num_nodes, num_edges = map(int, input().split())

# Adjacency list to store the undirected graph
adjacency_list = [[] for _ in range(num_nodes)]
# Map each edge (u, v) and (v, u) to its input index (0 to M-1)
edge_to_index = {}
# Initially paint all edges grey
painted_edges = ["G"] * num_edges

# Read and store all edges for undirected graph
for i in range(num_edges):
    u, v = [x-1 for x in map(int, input().split())]
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)
    edge_to_index[(u, v)] = i
    edge_to_index[(v, u)] = i
    
# A Function to build a graph and paint its edges alternately red and blue
visited = [False] * num_nodes
def paint_graph_edges(node, paint_red):
    visited[node] = True
    # Loop through all neighbours
    for neighbor in adjacency_list[node]:
        if not visited[neighbor]:
            # Get the index of the edge between current node and neighbor
            edge_index = edge_to_index[(node, neighbor)]
            painted_edges[edge_index] = "R" if paint_red else "B"
            # Recursively paint the next level with alternating color
            paint_graph_edges(neighbor, not paint_red)

# Traverse all components of the graph
for node in range(num_nodes):
    if not visited[node]:
        # Start painting from this node with red
        paint_graph_edges(node, paint_red=True)

# Output
print("".join(painted_edges))
