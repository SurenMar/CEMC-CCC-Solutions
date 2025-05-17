rows = int(input())
cols = int(input())

# create patch 2d list, and visited 2d list keep track of squares visited
patch = []
visisted = []
for i in range(rows):
    row = input()
    patch.append(row)
    visisted.append([False] * len(row))

# starting position
start_r = int(input())
start_c = int(input())

# helper function to return price of pumpkin based on size
def pumpkin_price(pumpkin):
    if pumpkin == 'S':
        return 1
    elif pumpkin == 'M':
        return 5
    else:
        return 10

# recursive flood fill algorithm
def flood_fill(r, c):
    # returns 0 if farmer is at an invalid position or spot is already visited
    if r < 0 or r >= rows or c < 0 or c >= cols or \
       patch[r][c] == '*' or visisted[r][c]:
        return 0
    else:
        visisted[r][c] = True   # Toggles square on
        # returns price of current pumpkin plus all adjecent squares
        return pumpkin_price(patch[r][c]) + flood_fill(r+1, c) + \
            flood_fill(r-1, c) + flood_fill(r, c+1) + flood_fill(r, c-1)
            
print(flood_fill(start_r, start_c))
