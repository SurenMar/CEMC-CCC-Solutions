# https://cemc.uwaterloo.ca/sites/default/files/documents/2020/2020CCCJrProblemSet.html

rows = int(input())
cols = int(input())
visited = []    # list to keep track of visited squares in room

# read room integers
room = [list(map(int, input().split())) for _ in range(rows)]

# helper function to find divisors of a number given two max value restrictions
def find_divs(n, r_cap, c_cap):
    divisors = []   # store all divisors
    for r in range(1, n+1):
        # check if r divides n, and r and c are below the cap
        if n % r == 0 and r <= r_cap and n // r <= c_cap:
            divisors.append([r, n // r])
    return divisors

# recursive function that checks if the room is escapable
def escape_room(row, col):
    # checks if row and col are on the bottom right square
    if row == rows and col == cols:
        return True
    # checks if current square was already visited to avoid infinite recursion
    elif [row, col] in visited:
        return False
    else:
        visited.append([row, col])  # adds current square to visited squares
        # finds all divisors of current square
        coords = find_divs(room[row-1][col-1], rows, cols)
        for coord in coords:
            # for every divisor combination, check if it leads to an escape
            if escape_room(coord[0], coord[1]):
                return True

# output (returns None if no escape is found)
if escape_room(1, 1):
    print('yes')
else:
    print('no')
                