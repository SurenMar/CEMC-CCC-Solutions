# https://cemc.uwaterloo.ca/sites/default/files/documents/2020/2020CCCSrProblems.html

sequence = input()

# Count each group
num_a = sequence.count('A')
num_b = sequence.count('B')
num_c = sequence.count('C')

# Tactic: start looping through sequence from the left, if a group doesnt
#   match what its supposed to be, then loop from the right and replace it with
#   the first instance the correct group.
# Move on to the next group if the current group has reached its number of occurences.

# Repeat this process 6 times, 1 for each permutation of A, B, C, and find the min swaps


permutations = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'] # Perms to go through
num_swaps = num_a + num_b + num_c # Max number of swaps possible

# Loop through each ordering of groups and find min swaps
for ordering in permutations:
    group1, group2, group3 = ordering[0], ordering[1], ordering[2]
    group_seen = 0 # Number of times current group is seen
    for letter in sequence:
        if 