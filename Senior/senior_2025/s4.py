# https://cemc.uwaterloo.ca/sites/default/files/documents/2025/2025CCCSrProblems.html

num_rooms, num_tunnels = map(int, input().split())

# Create graph of the dungeon
# Note: We dont use multiplcation to initialize the graph because that would
#   link all the list inside the graph together, but we need seperate lists
dungeon_graph = [[] for _ in range(num_rooms)]
for _ in range(num_tunnels):
    room1, room2, temp = map(int, input().split())
    dungeon_graph[room1-1].append((room2-1, temp))

# Recursive function to find the lowest cost path using:
#   boots current chilling level, coins spent, rooms visited, and current room
def find_path(chilling, coins_spent, visited, room):
    # Base case: User escapes
    if room == num_rooms-1:
        return coins_spent
    # Visited room: return None since this cannot be lowest path
    elif room in visited:
        return None
    # Find the next possible paths from current room
    else:
        visited.append(room)
        min_path = None
        for next_room in dungeon_graph[room]:
            # Check whether chilling matches tunnel temp and update trackers
            if next_room[1] == chilling:
                path_cost = find_path(chilling, coins_spent, visited, next_room[0])
            else:
                coins_spent += abs(next_room[1] - chilling)
                chilling = next_room[1]
                path_cost = find_path(chilling, coins_spent, visited, next_room[0])
            
            # Check path cost and update min path
            if min_path == None:
                min_path = path_cost
            elif path_cost != None:
                min_path = min(min_path, path_cost)
                
        return min_path
    
# Output
print(find_path(0, 0, [], 0))
                
                
            
    
