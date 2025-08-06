# https://cemc.uwaterloo.ca/sites/default/files/documents/2020/2020CCCSrProblems.html

num_obvs = int(input())
obvs = [tuple(map(int, input().split())) for _ in range(num_obvs)]

# Sort the observations
obvs.sort(key=lambda obv: obv[0])

# Loop through observations and find max speed difference
max_speed = 0
for i in range(1, num_obvs):
    time1, pos1 = obvs[i-1]
    time2, pos2 = obvs[i]
    # Calculate speed
    speed = abs(pos2 - pos1) / (time2 - time1)
    max_speed = max(max_speed, speed)

# Output
print(max_speed)