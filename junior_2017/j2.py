# https://cemc.uwaterloo.ca/sites/default/files/documents/2017/2017CCCJrProblemSet.html

n = int(input())
sum = n
# Add to sum and shift n each time
for _ in range(int(input())):
    n *= 10     # Shift n
    sum += n
    
# Output
print(sum)