# https://cemc.uwaterloo.ca/sites/default/files/documents/2015/2015CCCJrProblemSet.html

# Declare needed lists and dictionaries
friends = []
wait_times = {}
flags = {}

# A function with default param value w=1, increments the wait time for friends
def increase_wait(w=1):
    for friend in friends:
        if flags[friend]:
            wait_times[friend] += w

num_lines = int(input(""))
# Loops through all lines
while num_lines > 0:
    user_input = input()
    action = user_input[0]
    num = user_input[2:]
    # If user recieves set their flag to True and add friend in friends list 
    #   if the friend isnt in it
    if action == 'R':
        if num not in friends:
            friends.append(num)
            wait_times[num] = -1
        flags[num] = True
    # If user sends, change the flag
    elif action == 'S':
        flags[num] = False
    # If user waits, increment the wait times and skip the loop
    elif action == 'W':
        increase_wait(int(num))
        num_lines -= 1
        continue
    # Increase wait times for all friends
    increase_wait()
    num_lines -= 1

# Set wait time to -1 if the friend hasnt been replied to
for friend in friends:
    if flags[friend]:
        wait_times[friend] = -1

# Output
print(wait_times)