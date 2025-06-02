# https://cemc.uwaterloo.ca/sites/default/files/documents/2018/2018CCCJrProblemSet.html

spots = int(input())
yesterday = input()
today = input()

# Check if both spots contain a car
count = 0
for spot in range(spots):
    if yesterday[spot] == 'C' and today[spot] == 'C':
        count += 1
        
# output
print(count)