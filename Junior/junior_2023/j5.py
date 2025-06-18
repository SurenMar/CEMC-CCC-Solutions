# https://cemc.uwaterloo.ca/sites/default/files/documents/2023/2023CCCJrProblemSet.html

word = input()
rows = int(input())
cols = int(input())

# read grid
grid = []
for r in range(rows):
    row = input().split()
    grid.append(row)

# helper function to change directions at a right angle
def change_directions(dir):
    # for initial horizontal directions
    if dir[0] == 0:
        return [[1, 0], [-1, 0]]
    # for initial vertical directions
    elif dir[1] == 0:
        return [[0, 1], [0, -1]]
    # for initial diagonal directions
    else:
        return [[-dir[0], dir[1]], [dir[0], -dir[1]]]

# recursive function to check a path in grid.
#   letter_pos handles the current letter being processed in word
#   dir is the direction we are currently checking
#   dir_changed tells us if we have already changes directions
def check_grid(r, c, letter_pos, dir, dir_changed):
    # base case if letter doesnt match or if out of bounds
    if r < 0 or r == rows or c < 0 or c == cols or \
       grid[r][c] != word[letter_pos]:
        return 0
    # base case if entire word matches
    elif letter_pos == len(word) - 1 and grid[r][c] == word[letter_pos]:
        return 1
    # recursive case performed if current letter matches the actual word but
    #   the entire word still hasnt been checked yet
    else:
        flipped_path = 0        # words found after switching directions
        lp = letter_pos + 1     # temporary variable to avoid messiness
        # checking current direction
        straight_path = check_grid(r + dir[0], c + dir[1], lp, dir, dir_changed)
        
        # checking the flipped directions if we have not already done so and
        #   if we are not at the starting letter
        if not dir_changed and letter_pos != 0:
            dir_changes = change_directions(dir)
            dir1 = dir_changes[0]
            dir2 = dir_changes[1]
            flipped_path = \
                check_grid(r + dir1[0], c + dir1[1], lp, dir1, True) + \
                check_grid(r + dir2[0], c + dir2[1], lp, dir2, True)
        
        return flipped_path + straight_path

# check each letter in grid if it matches the word
words_found = 0
for r in range(rows):
    for c in range(cols):
        
        # find if the current letter leads to word by checking all directions
        #   including the diagonals
        words_found += \
            check_grid(r, c, 0, [1, 0], False) + check_grid(r, c, 0, [0, 1], False) + \
            check_grid(r, c, 0, [-1, 0], False) + check_grid(r, c, 0, [0, -1], False) + \
            check_grid(r, c, 0, [1, 1], False) + check_grid(r, c, 0, [1, -1], False) + \
            check_grid(r, c, 0, [-1, 1], False) + check_grid(r, c, 0, [-1, -1], False)

# output
print(words_found)