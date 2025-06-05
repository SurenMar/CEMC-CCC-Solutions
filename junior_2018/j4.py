# https://cemc.uwaterloo.ca/sites/default/files/documents/2018/2018CCCJrProblemSet.html

# Read table
n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

# This function checks if a table is in the desired format
def check_table(table):
    return table[0] == sorted(table[0]) and table[0][0] < table[1][0]

# This function rotates table clockwise
# Note: It does not matter whether we rotate clockwise or counterclockwise
def rotate_table(table, n):
    new_table = []
    # This nested for loop goes down the columns of the original table creating
    #   rows, and adding it to the new table
    for col in range(n):
        new_row = []
        # We countdown instead of just using reverse since using reverse
        #   would make it O(n^3)
        for row in range(n-1, -1, -1):
            new_row.append(table[row][col])
        new_table.append(new_row)
    return new_table

# Rotate through table until its in its desired format
while not check_table(table):
    table = rotate_table(table, n)
    
# Output
for row in table:
    for entry in row:
        print(entry, end=' ')
    print()