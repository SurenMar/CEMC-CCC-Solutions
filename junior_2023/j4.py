# https://cemc.uwaterloo.ca/sites/default/files/documents/2023/2023CCCJrProblemSet.html

cols = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))

# initialize total length of tape needed
tape = 0
if row1[0] == 1:
    tape = 3

# loop through row1 of tiles
for c in range(1, cols):
    # check if previous and current tile are wet
    if row1[c] == 1 and row1[c-1] == 1:
        tape += (2 - 1)     # add 2 new edges and remove 1 old edge
    
    # check if only current tile is wet
    elif row1[c] == 1:
        tape += 3           # add 3 new edges

# check first tile in row2
if row2[0] == 1 and row1[0] == 1:
    tape += (2 - 1)     # add 2 new edges and remove 1 old edge
elif row2[0] == 1:
    tape += 3           # add 3 new edges

# loop through row2 of tiles
for c in range(1, cols):
    # check if current tile and tile above are wet and if the tiles are odd 
    #   numbered since even numbered tiles dont share a common edge
    if row2[c] == 1 and row1[c] == 1 and (c+1) % 2 == 1:
        # check if previous tile is also wet
        if row2[c-1] == 1:
            tape += (1 - 2)     # add 1 new edge and remove 2 old edges
        else:
            tape += (2 - 1)     # add 2 new edges and remove 1 old edge
            
    # check if previous tile and current tile are wet
    elif row2[c] == 1 and row2[c-1] == 1:
        tape += (2 - 1)     # add 2 new edges and remove 1 old edge
    
    # check if only current tile is wet
    elif row2[c] == 1:
        tape += 3           # add 3 new edges
        
print(tape)
    