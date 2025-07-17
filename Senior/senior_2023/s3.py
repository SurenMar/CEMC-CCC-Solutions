# https://cemc.uwaterloo.ca/sites/default/files/documents/2023/2023CCCSrProblems.html

num_rows, num_cols, pdr_rows, pdr_cols = map(int, input().split())

# Poster design is impossible only if all rows need to be palindromes and 
#   the num_cols is even but pdr_cols is odd (or vice versa).
if (num_rows == pdr_rows and num_cols % 2 == 0 and pdr_cols % 2 == 1) or \
   (num_cols == pdr_cols and num_rows % 2 == 0 and pdr_rows % 2 == 1):
    print('IMPOSSIBLE')
    quit()

# Initialize grid
grid = [['a' for _ in range(num_cols)] for _ in range(num_rows)]

# Check if there will be 'free' squares in the grid
if num_rows != pdr_rows and num_cols != pdr_cols:
    for i in range(num_rows - pdr_rows):
        for j in range(num_cols - pdr_cols):
            grid[i][j] = 'b'    # Change free square to different letter
#  All rows are palindromes (no free squares)
elif num_rows == pdr_rows:
    # Reduce palindromic cols to desired amount (pdr_cols)
    left, right = 0, num_cols - 1
    pdr_count = num_cols - pdr_cols
    # Alter first row and eeliminate palindromic columns
    while pdr_count > 0:
        grid[0][left] = 'b'
        grid[0][right] = 'b'
        # Increment counters
        pdr_count -= 2
        # Only change middle column if only 1 more column is left
        if pdr_count == 1:
            left = num_cols // 2
            right = left
        else:
            left += 1
            right -= 1
            
#  All cols are palindromes (no free squares)
else:
    # Reduce palindromic rows to desired amount (pdr_rows)
    top, bottom = 0, num_rows - 1
    pdr_count = num_rows - pdr_rows
    while pdr_count > 0:
        grid[top][0] = 'b'
        grid[bottom][0] = 'b'
        # Increment counters
        pdr_count -= 2
        # Only change middle row if only 1 more rows is left
        if pdr_count == 1:
            top = num_rows // 2
            bottom = top
        else:
            top += 1
            bottom -= 1

# Output
for r in grid:
    for letter in r:
        print(letter, end=' ')
    print()
