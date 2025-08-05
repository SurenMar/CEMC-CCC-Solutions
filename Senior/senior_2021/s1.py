# https://cemc.uwaterloo.ca/sites/default/files/documents/2021/2021CCCSrProblems.html

num_wood = int(input())
heights = list(map(int, input().split()))
widths = list(map(int, input().split()))

area = 0
# Loop through all pieces of wood for fencing
for i in range(num_wood):
    min_height = min(heights[i], heights[i+1])
    max_height = max(heights[i], heights[i+1])
    # Calculate area of rectangle and traingel seperately
    rectangle = min_height * widths[i]
    triangle = (max_height - min_height) * widths[i] / 2
    area += rectangle + triangle

# Output
print(area)