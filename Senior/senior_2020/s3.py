# https://cemc.uwaterloo.ca/sites/default/files/documents/2020/2020CCCSrProblems.html

needle = input()
haystack = input()

needle_len = len(needle)

# Count the number of appearences of each letter in needle
letters_count = dict()
for letter in needle:
    letters_count[letter] = letters_count.get(letter, 0) + 1

# A function to see if total_letters is the same as letters_count
def is_perm():
    for letter in letters_count.keys():
        if total_letters[letter] != letters_count[letter]:
            return False
    return True

# Analyze initial needle_len characters in haystack
total_letters = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
filter = ''
for i in range(needle_len):
    total_letters[haystack[i]] += 1
    filter += haystack[i]

# Filter through haystack and count distinct permutations
perm_count = 1 if is_perm() else 0
perms = {filter: True}
for i in range(needle_len, len(haystack)):
    # Add the letter in front of the filter and remove the letter at the back
    total_letters[haystack[i]] += 1
    total_letters[haystack[i - needle_len]] -= 1
    # Do same thing to teh filter
    filter += haystack[i]
    filter = filter[1:]
    # Check if current filter is a disticnt permutation
    if is_perm() and not perms.get(filter):
        perms[filter] = True
        perm_count += 1

# Output
print(perm_count)
    
