# https://cemc.uwaterloo.ca/sites/default/files/documents/2019/2019CCCSrProblems.html

square = [list(input().split()) for _ in range(3)]

new_square = [[], [], []]

def find_missing_term(missing_idx, lst):
    if missing_idx == 0:
        val1, val2 = int(lst[1]), int(lst[2])
        return val1 - (val2 - val1)
    elif missing_idx == 1:
        val1, val2 = int(lst[0]), int(lst[2])
        return (val2 - val1) // 2 + val1
    else:
        val1, val2 = int(lst[0]), int(lst[1])
        return val2 - val1 + val2

# Find rows with only 1 X
for row in square:
    if row.count('X') == 1:
        i = row.index('X')
        row[i] = str(find_missing_term(i, row))

# Same thing but for columns
square = list(map(list, zip(*square)))  # Transpose square
for col in square:
    if col.count('X') == 1:
        i = col.index('X')
        col[i] = str(find_missing_term(i, col))

square = list(map(list, zip(*square)))  # Revert square back
print(square)

# NOTE: THIS SOLUTION DOESNT WORK WITH:
# X X 1
# 2 2 2
# 4 6 3
# (top row not a sequence)
