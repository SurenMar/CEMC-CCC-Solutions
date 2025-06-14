# https://cemc.uwaterloo.ca/sites/default/files/documents/2017/2017CCCJrProblemSet.html

num_wood = int(input())
wood = list(map(int, input().split()))

# Find all possible board lengths (combinations of wood pieces)
combinations = []
for i, wood_piece1 in enumerate(wood[:-1]): # Exclude the last element
    for wood_piece2 in wood[i+1:]:
        combinations.append(wood_piece1 + wood_piece2)
distincts = list(set(combinations))      # Remove duplicates

# Count how many times each length appears and track the max length
length_counter = [0] * len(distincts)
max_length = 0
for length in combinations:
    # Check if length appears in the distinct lengths
    if length in distincts:
        i = distincts.index(length)     # Get index
        length_counter[i] += 1          # Increment coutner
        if length_counter[i] > max_length:
            max_length = length_counter[i]
            
# Check how many times the max appears in length_counter
max_appearance = length_counter.count(max_length)

# Output
print(max_length, max_appearance)

# Note: I did not do ALL of this in a sigle nested for loop because this
#   program would have been O(n^3) which is too long.
        