# https://cemc.uwaterloo.ca/sites/default/files/documents/2023/2023CCCSrProblems.html

num_rows, num_cols, pdr_rows, pdr_cols = map(int, input().split())

# Poster design is impossible only if all rows need to be palindromes, and 
#   an odd number of columns need to be palindromes.
if num_rows == pdr_rows and pdr_cols % 2 == 1:
    print('IMPOSSIBLE')

# Initialize grid
grid = [['a' for _ in range(num_cols)] for _ in range(num_rows)]

# Create algorithm by initializing grid with all 'a' then altering entries as needed

# CHECK WHAT HAPPENS IF TOTAL COLUMNS IS SO LARGE THAT NOT ALL LETTERS IN ALPHABET ARE ENOUGH => IMPOSSIBLE
