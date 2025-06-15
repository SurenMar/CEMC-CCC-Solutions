# https://cemc.uwaterloo.ca/sites/default/files/documents/2016/2016CCCJrProblemSet.html

# Read square
square = [list(map(int, input().split())) for _ in range(4)]

# Find sum of first row
magic_sum = sum(square[0])

# Check if the rows match the magic sum
for row in square:
    if sum(row) != magic_sum:
        print('not magic')
        exit()
        
# Check if the columns match the magic sum
for col in range(4):
    col_sum = 0
    for row in range(4):
        col_sum += square[row][col]
    
    if col_sum != magic_sum:
        print('not magic')
        exit()

# Output
print('magic')