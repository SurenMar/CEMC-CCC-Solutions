# https://cemc.uwaterloo.ca/sites/default/files/documents/2017/2017CCCJrProblemSet.html

total_time = int(input())

# Function that finds all sequences up until the given end time
def find_sequences(end_time):
    # Check if end time is in 12:XX but before the first sequence
    if end_time < 34:
        return 0
    # Check if end time is in 12:XX but after the first sequence
    elif end_time <= 60:
        return 1
    
    # Start time
    hour = 1
    minute = 0
    # End time
    end_hour = end_time // 60
    end_minute = end_time - end_hour * 60
    sequences = 1
    # Loop until end time is reached
    while hour != end_hour or minute != end_minute:
        # Check if hour is single digit and if common difference exists
        if hour < 10 and \
        (minute // 10) - hour + (minute // 10) == minute % 10:
            sequences += 1
        # Check if hour is double digit and if common difference exists
        elif hour >= 10 and \
            (hour // 10) - (hour % 10) + (hour // 10) == minute // 10:
            sequences += 1
        
        # Increment time
        if minute == 59:
            hour += 1
            minute = 0
        else:
            minute += 1
    return sequences

# Calculate number of 12-hour cycles and the leftover time after those cycles
MINUTES_IN_12_HOURS = 11 * 60 + 59
num_cycles = total_time // MINUTES_IN_12_HOURS
leftover_time = total_time - MINUTES_IN_12_HOURS * num_cycles

# Find total sequences
sequences = num_cycles * find_sequences(MINUTES_IN_12_HOURS)
sequences += find_sequences(leftover_time)

# Output
print(sequences)
