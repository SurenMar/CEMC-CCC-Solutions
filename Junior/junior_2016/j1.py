# https://cemc.uwaterloo.ca/sites/default/files/documents/2016/2016CCCJrProblemSet.html

# Count number of wins
win_count = 0
for _ in range(6):
    if input() == 'W':
        win_count += 1

# Output
if win_count == 0:
    print(-1)
elif win_count <= 2:
    print(3)
elif win_count <= 4:
    print(2)
else:
    print(1)