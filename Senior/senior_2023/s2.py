# https://cemc.uwaterloo.ca/sites/default/files/documents/2023/2023CCCSrProblems.html

num_mounts = int(input())
heights = list(map(int, input().split()))

# Initialize asymmetric values
asym_values = [0]

# A function that finds asymmetrical sum via 2-pointer approach
def find_asym_value(start, end):
    sum = 0
    while start < end:
        sum += abs(heights[start] - heights[end])
        start += 1
        end -= 1
    return sum

# Loop through each possible filter length
for i in range(2, num_mounts + 1):
    min_sum = None
    # Loop through every consecutive filter of length i in heights list
    for start in range(num_mounts - i + 1):
        # Update min_sum for current filter length if needed
        sum = find_asym_value(start, i + start - 1)
        if min_sum == None or sum < min_sum:
            min_sum = sum
    asym_values.append(min_sum)

# Output
for asym_value in asym_values:
    print(asym_value, end=' ')
print()