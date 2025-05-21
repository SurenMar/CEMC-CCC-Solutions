# https://cemc.uwaterloo.ca/sites/default/files/documents/2021/2021CCCJrProblemSet.html

num = input()       # read first code as a string
directions = []     # directions list

# determine directions as long as code isnt 99999
while num != '99999':   
    sum = int(num[0]) + int(num[1])     # sum of first two digits
    # total steps to take
    steps = int(num[2]) * 100 + \
        int(num[3]) * 10 + \
        int(num[4])
    
    # check if sum and modify dir except if sum is 0
    if sum % 2 == 1:
        dir = 'left'
    elif sum % 2 == 0 and sum != 0:
        dir = 'right'
    
    directions.append(f"{dir} {steps}")     # add current direction to list
    num = input()                           # read next code as a string

# output
for direction in directions:
    print(direction)
    
    