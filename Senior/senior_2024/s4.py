# https://cemc.uwaterloo.ca/sites/default/files/documents/2024/2024CCCSrProblems.html

num_nodes, num_roads = map(int, input().split())

# Create double ended graph of roads and hashmap for the paint on each road
roads = {}
road_graph = [[] for _ in range(num_nodes)]
for _ in range(num_roads):
    node1, node2 = map(int, input().split())
    min_node = min(node1-1, node2-1)
    max_node = max(node1-1, node2-1)
    roads[(min_node, max_node)] = 'G'
    road_graph[min_node].append(max_node)
    road_graph[max_node].append(min_node)

print(road_graph)

# A function to see if a triangular cyclic exists through node and next_node
def is_triangle(node, next_node):
    for next_next_node in road_graph[next_node]:
        if set(node, next_node, next_next_node) not in triangles_visited and \
           node in road_graph[next_next_node]:
            triangles_visited.append(set(node, next_node, next_next_node))
            return next_next_node
    return None

def colour_triangle(node, next_node, next_next_node):
    pass

# Loop through each node and paint the road it creates either B, R, or keep it G
triangles_visited = []
for node in range(num_nodes):
    for i, next_node in enumerate(road_graph[node]):
        next_next_node = is_triangle(node, next_node)
        if next_next_node:
            pass

# Output
paint = ''.join(roads.values())
print(paint)

# ALL PATHS MUST HAVE AT LEATS ONE COLOURED ROAD BRANCHING OFF

# Given 2 nodes, if another node is added to it, colour the paths based on
#   the path of the first 2 nodes.
            
