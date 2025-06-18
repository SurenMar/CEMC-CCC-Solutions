# https://cemc.uwaterloo.ca/sites/default/files/documents/2018/2018CCCJrProblemSet.html

# We use deque for queue and not regular list because in list, popping an
#   element will be O(n) each pop
from collections import deque

# Read and initialize graph
n = int(input())
graph = []
ending_pages = []

# Build graph and record which pages are ending pages
for i in range(n):
    line = list(map(int, input().split()))
    num_choices = line[0]
    if num_choices == 0:
        ending_pages.append(i + 1)
    graph.append(line[1:])  # Add choices from current page to graph

# Create visited and steps to keep track pages visited and steps taken
visited = [False] * (n + 1)
steps = [0] * (n + 1)

# Create deque and add page 1 to start of queue
queue = deque()
queue.append(1)
visited[1] = True

# Keep track of minimum steps to an ending page
min_steps = None

# Loop queue until its empty checking whether a page is an ending page or
#   if a neighbour hasnt been visited
while queue:
    current = queue.popleft()
    # If this page is an ending page, update min_steps if it's smaller
    if current in ending_pages:
        if min_steps is None or steps[current] < min_steps:
            min_steps = steps[current]
    # Visit all neighboring pages
    for neighbor in graph[current - 1]:
        if not visited[neighbor]:
            visited[neighbor] = True
            steps[neighbor] = steps[current] + 1
            queue.append(neighbor)

# Check if all pages were visited (i.e., reachable from page 1)
all_reachable = True
for i in range(1, n + 1):
    if not visited[i]:
        all_reachable = False
        break

# Output
print("Y" if all_reachable else "N")
# Add 1 to steps to count the number of pages (not just moves)
print(min_steps + 1)