# https://cemc.uwaterloo.ca/sites/default/files/documents/2018/2018CCCSrProblems.html

rows, cols = map(int, input().split())

# Read grid
dots = []
start = []
grid = []
for r in range(rows):
    row = list(input())
    for c in range(cols):
        if row[c] == 'S':
            start = [r, c]
        elif row[c] == '.':
            dots.append([r, c])

# Recursive function to find shortest distance from pos to dest
def shortest_dist(grid, pos, dest, dist):
    if pos == dest:
        return dist
    elif grid[pos[0]][pos[1]] == 'W':
        return float('inf')
    elif grid[]
    # have all other case

# Loop through and find shortest distacne to each dot
for dot in dots:
    min_dist = shortest_dist(grid, start, dot, float('inf'))
    # Output
    print(min_dist) if min_dist != float('inf') else print(-1)
