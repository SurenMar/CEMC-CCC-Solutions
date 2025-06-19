# https://cemc.uwaterloo.ca/sites/default/files/documents/2025/2025CCCSrProblems.html

a, b, x, y = map(int, input().split())

# Calculate minumum perimter by overlapping the bases of each painting
# Note it doesnt matter which side we overlapp, both result in the
#   minimum perimeter
perimeter = 2 * max(a, x) + 2 * (b + y)

# Output
print(perimeter)