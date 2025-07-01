# https://cemc.uwaterloo.ca/sites/default/files/documents/2025/2025CCCSrProblems.html

# Initialize variables
modulus = (10 ** 6) + 3
ans = 0
schedule = []   # Element format: [task_num, s, t]
min_times = []

# A function to calculate the minimum finish time of the scheudle
def min_finish():
    pass

# A function that returns the index of the task with desired task_num
# Assumes that task num always exists
def find_task(task_num):
    for i, task in enumerate(schedule):
        if task[0] == task_num:
            return i

# Loop through each schedule update
for task_num in range(int(input())):
    line = list(map(int, input().split()))
    # Check type of update
    if line[0] == 'A':
        s = (line[1] + ans) % modulus
        t = (line[2] + ans) % modulus
        # Insert task into scheudle
        schedule.insert([task_num, s, t])
    else:
        i = (line[1] + ans) % modulus
        # Delete desired task from schedule
        del schedule[find_task(i-1)]
    # Append new min_finish time to list
    min_times.append(min_finish())
    
# Output
for min_time in min_times:
    print(min_time)
    
    
