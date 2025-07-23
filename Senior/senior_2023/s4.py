# https://cemc.uwaterloo.ca/sites/default/files/documents/2023/2023CCCSrProblems.html

num_nodes, num_paths = map(int, input().split())

# Store all roads as tuples: (length, cost, node1, node2)
edges = []
for _ in range(num_paths):
    u, v, l, c = map(int, input().split())
    edges.append((l, c, u - 1, v - 1))  # convert to 0-based indexing

# Sort by shortest length first, then by lowest cost
edges.sort()

# Graph of currently chosen roads (those that maintain shortest paths)
# Each entry: [ (neighbor_node, road_length), ... ]
graph = [[] for _ in range(num_nodes)]

# Tracks total cost of maintaining roads required for shortest paths
total_cost = 0

# Function to find the shortest path from start to end using current roads
# Only uses the roads that are in 'graph'
def shortest_distance(start, end, limit):
    visited = [False] * num_nodes
    distances = [float('inf')] * num_nodes
    distances[start] = 0

    # Simple queue
    queue = [start]

    # Performs dijkstra's algorithm
    while queue:
        # Find the node in the queue with the smallest distance
        min_idx = 0
        for i in range(1, len(queue)):
            if distances[queue[i]] < distances[queue[min_idx]]:
                min_idx = i

        node = queue.pop(min_idx)
        visited[node] = True

        # Early stop if we go past limit
        if distances[node] > limit:
            break

        # Stop if we reached destination
        if node == end:
            return distances[node]

        # Explore neighbors
        for neighbor, length in graph[node]:
            if not visited[neighbor] and distances[node] + length < distances[neighbor]:
                distances[neighbor] = distances[node] + length
                # Add to queue if not already there
                if neighbor not in queue:
                    queue.append(neighbor)

    return distances[end]

# Go through each road, shortest first
for length, cost, u, v in edges:
    # Check if current shortest path between u and v is greater than this road
    current = shortest_distance(u, v, length)

    # If it's longer, we must add this road to maintain shortest paths
    if current > length:
        graph[u].append((v, length))
        graph[v].append((u, length))
        total_cost += cost

# Output
print(total_cost)
