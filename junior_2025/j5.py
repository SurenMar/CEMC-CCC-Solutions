# https://cemc.uwaterloo.ca/sites/default/files/documents/2025/2025CCCJrProblemSet.html

rows = int(input())
cols = int(input())
m = int(input())

# create grid
grid = []
n = 1
for i in range(rows):
    # create row
    row = []
    for j in range(cols):
        row.append(n)
        n += 1
        # reset n
        if n > m:
            n = 1
    grid.append(row)    # add row to grid

# recursive function to find optimal path given a row and col
def find_path(row, col):
    # base case
    if row == rows - 1:
        return grid[row][col]
    # left most column on the grid
    elif col == 0:
        return grid[row][col] + min(find_path(row + 1, col),
                                    find_path(row + 1, col + 1))
    # right most column on the grid
    elif col == cols - 1:
        return grid[row][col] + min(find_path(row + 1, col - 1),
                                    find_path(row + 1, col))
    # middle of the grid
    else:
        return grid[row][col] + min(find_path(row + 1, col - 1),
                                    find_path(row + 1, col),
                                    find_path(row + 1, col + 1))
        
# find optimal path among all starting points on first row
min_path = find_path(0, 0)
for col in range(1, cols):
    min_path = min(min_path, find_path(0, col))
    
print(min_path)