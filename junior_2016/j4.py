# https://cemc.uwaterloo.ca/sites/default/files/documents/2016/2016CCCJrProblemSet.html

hour, minute = map(int, input().split(':'))

commute_left = 120              # Keeps track of the commute time remaining in minutes
cur_time = hour * 60 + minute   # Keeps track of the current time

# Check if hour is between 00 and 07
if hour < 7:
    # Subtract commute time from the time it takes from the current hour to
    #   get to 7 am
    time_taken = 7 * 60 - cur_time
    commute_left -= time_taken
# Check if hour is in the first rush hour traffic window
elif hour < 10:
    # Same arithmetic as above, but now half it because the speed is halved
    time_taken = 10 * 60 - cur_time
    commute_left -= time_taken // 2
# Check if hour is between 10 and 15
elif hour < 15:
    # Subtract commute time from the time it takes from the current hour to
    #   get to 3 pm
    time_taken = 15 * 60 - cur_time
    commute_left -= time_taken
# Check if hour is in the second rush hour traffic window
elif hour < 19:
    # Same arithmetic as above, but now half it because the speed is halved
    time_taken = 19 * 60 - cur_time
    commute_left -= time_taken // 2
# Fiona wont encounter any rush hour traffic past the second window
else:
    commute_left = 0
    time_taken = 120

print(time_taken)
cur_time += time_taken  # Compute current time based on time taken

# Check if there is any more commuting to do
if commute_left <= 0:
    # Output
    hour = (hour + 2) % 24
    print(f"{hour:02}:{minute:02}")
    exit()
    
# Here, we take advantage of the fact that the commute time is guaranteed to
#   be filled out after the next computation, so theres no point finding the
#   remaining commute time remaining

# Set hour to cur_time values for easy access in if expressions
hour = cur_time // 60

# Check if hour is in first rush hour traffic window
if hour < 10:
    cur_time += commute_left * 2
# Check if hour is between the rush hour traffic windows
elif hour < 15:
    cur_time += commute_left
# The hour must be in the second rush hour traffic window
else:
    cur_time += commute_left * 2
    
# Output
print(f"{cur_time // 60:02}:{cur_time % 60:02}")
    
            
    