# https://cemc.uwaterloo.ca/sites/default/files/documents/2019/2019CCCSrProblems.html

# Helper function to flip square horizontally
def horizontal(square):
    new_square = [square[1], square[0]]
    return new_square

# Helper function to flip square vertically
def vertical(square):
    new_square = [list(reversed(square[0])), list(reversed(square[1]))]
    return new_square

# Go thorugh each flip and modify square
square = [[1, 2], [3, 4]]
flips = input()
for flip in flips:
    if flip == 'H':
        square = horizontal(square)
    else:
        square = vertical(square)
        
# Output
print(f"{square[0][0]}, {square[0][1]}")
print(f"{square[1][0]}, {square[1][1]}")