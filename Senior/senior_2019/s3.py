# https://cemc.uwaterloo.ca/sites/default/files/documents/2019/2019CCCSrProblems.html

square = [list(input().split()) for _ in range(3)]

# Deep copies the square
def deep_copy(square, new_square):
    for i in range(3):
        new_square[i][0] = square[i][0]
        new_square[i][1] = square[i][1]
        new_square[i][2] = square[i][2]


# Finds and fills in the missing term in a row or column
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
def fill_row(square):
    for row in square:
        if row.count('X') == 1:
            i = row.index('X')
            row[i] = str(find_missing_term(i, row))

# Same thing but for columns
def fill_col(square):
    square = list(map(list, zip(*square)))  # Transpose square
    for col in square:
        if col.count('X') == 1:
            i = col.index('X')
            col[i] = str(find_missing_term(i, col))
    square = list(map(list, zip(*square)))  # Revert square back

new_square = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Fill rows and columns until square is complete
while 'X' in square[0] or 'X' in square[1] or 'X' in square[2]:
    deep_copy(square, new_square)
    fill_row(square)
    fill_col(square)
    # Check if square has no rows and columns with at least 2 numbers
    if square == new_square:
        print('here')
        # Check rows
        for i, row in enumerate(square):
            elem = 0
            for item in row:
                if item != 'X':
                    elem = item
                    break
            square[i] = [elem] * 3
            print(elem, row)
        # Check columns
    elif square == new_square:
        print('here2')
        square = list(map(list, zip(*square)))  # Transpose square
        for i, col in enumerate(square):
            elem = 0
            for item in col:
                if item != 'X':
                    elem = item
                    break
            square[i] = [elem] * 3
        square = list(map(list, zip(*square)))  # Revert square back
    print('-------------')
    print(square)
    print(new_square)

# Output
for row in square:
    for elem in row:
        print(elem, end=' ')
    print()
