# https://cemc.uwaterloo.ca/sites/default/files/documents/2025/2025CCCSrProblems.html

rle_output = input()
pos = int(input())

# We use the fact that the length of the output will always be even since
#   theres a pair (letter and number) to access the number in each pair and
#   find the length of the orginal sequence pattern
sequence_length = 0
current_number = 0
for c in rle_output:
    # If we encounter a letter, add the current number to sequence total
    if c.isalpha():
        sequence_length += current_number
        current_number = 0
    # If we encounter a number, 'add' it to the current number
    else:
        current_number = current_number * 10 + int(c)

# Add remaining number to sequence length
sequence_length += current_number

# Find the position of the character relative to a single pattern
char_pos = (pos + 1) % sequence_length

# Find the character at position char_pos in a single pattern of the sequence
#   by finding the first prefix sum value thats greater than char_pos
prefix_sum = 0
current_number = 0
current_letter = rle_output[0]
for c in rle_output:
    # If we encounter a letter, add the current number to prefix sum and
    #   update the current letter
    if c.isalpha():
        prefix_sum += current_number
        current_number = 0
        # Check if prefix sum is greater than the specified char position
        if prefix_sum >= char_pos:
            # Output
            print(current_letter)
            exit()
        # Update current letter
        current_letter = c
    # If we encounter a number, 'add' it to the current number
    else:
        current_number = current_number * 10 + int(c)
        
# If no letter has been printed, then it must be the last character
print(current_letter)


        
