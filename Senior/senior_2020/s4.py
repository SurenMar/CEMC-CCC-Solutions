# https://cemc.uwaterloo.ca/sites/default/files/documents/2020/2020CCCSrProblems.html

sequence = list(input())
seq_len = len(sequence)

# Count each group
letter_counts = [
    sequence.count('A'),
    sequence.count('B'),
    sequence.count('C')
]
permutations = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'] # Perms to go through
min_swaps = sum(letter_counts) # Max number of swaps possible

# Loop through each ordering of groups and find min swaps
for ordering in permutations:
    seq_copy = sequence[:]
    curr_swaps = 0
    # Number of times current group is seen
    seen_count = 1 if seq_copy[-1] == ordering[0] else 0
    curr_letter = 0 # Current group
    i = 0
    while not (curr_letter == 2 and seen_count == letter_counts[2]):
        if seen_count == letter_counts[curr_letter]:
            curr_letter += 1
            seen_count = 0
        elif seq_copy[i] == ordering[curr_letter]:
            seen_count += 1
            i += 1
        else:
            # Swap curr letter with the first occurence of correct letter
            # Skip last letter if its the first group (circular ordering)
            j = seq_len - 2 if seq_copy[-1] == ordering[0] else seq_len - 1
            while seq_copy[j] != ordering[curr_letter]:
                j -= 1
            seq_copy[i], seq_copy[j] = seq_copy[j], seq_copy[i]
            curr_swaps += 1
            seen_count += 1
            i += 1
    min_swaps = min(min_swaps, curr_swaps)

# Output
print(min_swaps)