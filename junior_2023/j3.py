# https://cemc.uwaterloo.ca/sites/default/files/documents/2023/2023CCCJrProblemSet.html

attendance = [0, 0, 0, 0, 0]        # List counter that keeps track of each day
for i in range(int(input())):
    days = input()                  # Users availability
    for j in range(len(days)):
        if days[j] == 'Y':
            attendance[j] += 1      # Increment attendance for day j if needed
            
# Pretty print all max days
comma = False               # Flag to know when comma should be printed
max_day = max(attendance)   # Maximum days in attendance
for i in range(5):
    if attendance[i] == max_day and comma:  # Place comma if a day has already
                                            #   been written down
        print(f",{i+1}", end='')
    elif attendance[i] == max_day:
        print(i+1, end='')
        comma = True
        
print()