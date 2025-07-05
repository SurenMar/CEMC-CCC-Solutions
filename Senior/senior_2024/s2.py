# https://cemc.uwaterloo.ca/sites/default/files/documents/2024/2024CCCSrProblems.html

# Read strings in 2D list
num_strings, string_len = map(int, input().split())
strings = [input() for _ in range(num_strings)]


# Analyze each string and print T or F
for string in strings:
    # Initialize output and hashmap of each letter and its number of appearances
    letters_seen = {}   
    output = 'T'
    for letter in string:
        # Increase or initialize count of each letter in string
        if letter in letters_seen:
            letters_seen[letter] += 1
        else:
            letters_seen[letter] = 1
    
    # Check if any consecutive letters are both heavy or both light
    for i in range(1, string_len):
        if (letters_seen[string[i-1]] == 1 and letters_seen[string[i]] == 1) or \
           (letters_seen[string[i-1]] > 1 and letters_seen[string[i]] > 1):
            output = 'F'
            break
        
    # Output
    print(output)