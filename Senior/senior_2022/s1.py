# https://cemc.uwaterloo.ca/sites/default/files/documents/2022/2022CCCSrProblems.html

n = int(input())

LCM = 4 * 5     # LCM of 4 and 5

# Function to determine if partition is possible
def is_mix(target):
    for x in range(target // 4 + 1):
        if (target - x * 4) % 5 == 0:
            return True
    return False

# n is multiple of LCM
if n % LCM == 0:
    partitions = (n // LCM) + 1
# n is multiple of either 4 or 5
elif n % 4 == 0 or n % 5 == 0:
    partitions = 1
# n is a mix of 4 or 5
elif is_mix(n):
    partitions = 1
else:
    partitions = 0
    
# Output
print(partitions)