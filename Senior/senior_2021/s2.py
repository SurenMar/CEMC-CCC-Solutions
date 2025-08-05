# https://cemc.uwaterloo.ca/sites/default/files/documents/2021/2021CCCSrProblems.html

rows = int(input())
cols = int(input())

# draw canvas: False = Black; True = Gold
canvas = [[False] * cols for _ in range(rows)]

# read distinct choices and keep track of number of row and col strokes
choices = []
row_strokes = 0
col_strokes = 0
for _ in range(int(input())):
    choice = input().split()
    # remove choice if current choice has already been made since two strokes
    #   on the same row/col cancel each other out
    if choice in choices:
        choices.remove(choice)
        # increment stroke counts
        if choice[0] == 'R':
            row_strokes -= 1
        else:
            col_strokes -= 1
    else:
        choices.append(choice)
        # increment stroke counts
        if choice[0] == 'R':
            row_strokes += 1
        else:
            col_strokes += 1
            
# count total gold pieces by removing tiles that have been intersected.
# note that a tile has been painted over at most twice since we didnt count
#   duplicate choice, in which case the tile is currently black
intersections = row_strokes * col_strokes
golds = row_strokes * cols + col_strokes * rows - intersections * 2
# we subtract intersections twice to account for double counting

# output
print(golds)