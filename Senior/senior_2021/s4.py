# https://cemc.uwaterloo.ca/sites/default/files/documents/2021/2021CCCSrProblems.html

num_stations, num_walkways, num_swaps = map(int, input().split())

# Read walkways as a graph
walkways = [[] for _ in range(num_stations)]
for _ in range(num_walkways):
    s1, s2 = map(int, input().split())
    walkways[s1 - 1].append(s2 - 1)

# Read stations and swaps
stations = list(map(int, input().split()))
swaps = [tuple(map(int, input().split())) for _ in range(num_swaps)]

# Swaps two elements in a list
def swap(i1, i2, lst):
    lst[i1], lst[i2] = lst[i2], lst[i1]
    return lst

# Find shortest path time for each day
min_times = []
for day in swaps:
    # Swap the stations
    stations[day[0] - 1], stations[day[1] - 1] = \
    stations[day[1] - 1], stations[day[0] - 1]
    min_time = 0
    # Loop through current train route
    s = 0
    visited = []
    while stations[s] != num_stations:
        visited.append(stations[s] - 1)
        # Search neighbours and find best next move
        best_move_found = False
        # print(walkways[s])
        for neighbour in walkways[stations[s] - 1]:
            # Check if neighbour doesnt jump over sN and its not visited
            if neighbour not in visited and \
               stations.index(num_stations) >= stations.index(neighbour + 1):
                min_time += 1
                s = stations.index(neighbour + 1)
                best_move_found = True
                break
        # No best move is found from walkways
        if not best_move_found:
            min_time += 1
            s += 1
    min_times.append(min_time)

# Output
for min_time in min_times:
    print(min_time)
