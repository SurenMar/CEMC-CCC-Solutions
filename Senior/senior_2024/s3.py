# https://cemc.uwaterloo.ca/sites/default/files/documents/2024/2024CCCSrProblems.html

length = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compress B to not have any adjecent duplicates
B_copy = [B[0]]
for num in B:
    if num != B_copy[-1]:
        B_copy.append(num)

# If the numbers in A can form a subsequence of B_copy in the order they
#   are in, then A is transformable
b_index = 0
b_length = len(B_copy)
for i in range(length):
    if b_index == b_length:
        break
    elif A[i] == B_copy[b_index]:
        b_index += 1

# Check if the above comment is true
if b_index == b_length:
    print('YES')
else:
    print('NO')
    exit()
    
# Store swipe moves and count
moves = []
moves_count = 0
# Initialize l, r, and D
left_pos = 0
right_pos = 0
swipe = ''
for i in range(length):
    # Check if current letters dont match
    if A[i] != B[i]:
        # Set the swipe position and update right position
        if i == 0:
            swipe = 'L'
        elif i == length-1:
            swipe = 'R'
        elif not swipe and B[i] == B[i-1]:
            swipe = 'R'
        elif not swipe and B[i] == B[i+1]:
            swipe = 'L'
        right_pos = i
    # Check if letters now match and swipe is right
    elif swipe == 'R':
        moves_count += 1
        moves.append([swipe, left_pos, right_pos])
        left_pos = i
        swipe = ''
    # Check if letters now match and swipe is left
    elif swipe == 'L':
        moves_count += 1
        moves.append([swipe, left_pos+1, right_pos+1])
        left_pos = i
        swipe = ''
    # Check if swipe is empty
    else:
        left_pos = i

# Update moves for any remaining swipe that has not been added
if swipe:
    moves_count += 1
    moves.append([swipe, left_pos, right_pos])

# Output
print(moves_count)
for i in range(moves_count):
    print(f"{moves[i][0]} {moves[i][1]} {moves[i][2]}") 
