# https://cemc.uwaterloo.ca/sites/default/files/documents/2023/2023CCCSrProblems.html

# You will need to track visited squares as well as have some sort of path
#   length counter that will keep track of the length of a path back to a 
#   certain point in the search

# When deciding what path to visit from a set of new ones, pick the shortest
#   one, then the lowest cost

# Used to insert elements in a list while keeping the list sorted
from bisect import bisect_left

num_nodes, num_paths = map(int, input().split())

# Read graph
graph = [[] for _ in range(num_nodes)]
for _ in range(num_paths):
    node1, node2, length, cost = map(int, input().split())
    graph[node1].append((node2, length, cost))

# Finds the shortest path that can be taken.
def shortest_path(possible_paths):
    min_idx = 0
    for i in range(1, len(possible_paths)):
        if possible_paths[i][1] < possible_paths[min_idx][1]:
            min_idx = i
    return min_idx
        
# Recursive function to find most optimal path in graph
def find_path(node, num_visited, possible_paths, total_cost, prefix_length):
    """
    num_visted: number of all visited paths
    possible_paths: unique list of all current paths that can be taken
        element fromat: (destination_node, path_length, cost)
    total_cost: total cost of maintaining the chosen paths
    prefix_length: hashmap of prefix sums of path lengths
    """
    # Base case
    if num_visited == num_nodes:
        return total_cost
    else:
        # Update possible paths
        for neighbours in graph[node]:
            possible_paths.append(neighbours)
        # Remove duplicates and find shortest path
        possible_paths = list(set(possible_paths))
        min_idx = shortest_path(possible_paths)
          