# https://cemc.uwaterloo.ca/sites/default/files/documents/2017/2017CCCJrProblemSet.html

start = list(map(int, input().split()))
end = list(map(int, input().split()))
charge = int(input())

# We use the logic that if when we reach the destination in the shortest line
#   possible and the charge left is an odd number, then its impossible to reach
#   the end with no charge left. This is because we cannot move diagonally

path = abs(start[0] - end[0]) + abs(start[1] - end[1])
# Check if shortest path is greater than charge
if path > charge:
    print('N')
# Check if charge left is odd
if (charge - path) % 2 == 1:
    print('N')
else:
    print('Y')

