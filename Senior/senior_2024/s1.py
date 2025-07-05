# https://cemc.uwaterloo.ca/sites/default/files/documents/2024/2024CCCSrProblems.html

people = int(input())
# List of all people on first side of table
numbers = [int(input()) for _ in range(people // 2)]
count = 0

# Check if two opposite people have same number
for i in range(people // 2):
    # Check if the number of the i'th person on second half of table
    #   matches their opposite's on the first half
    if numbers[i] == int(input()):
        count += 2
        
# Output
print(count)
        


    