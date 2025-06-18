# https://cemc.uwaterloo.ca/sites/default/files/documents/2016/2016CCCJrProblemSet.html

word = input()

# A function to check if a word is a palindrome by comparing it to its reverse
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

# Nested loop that checks every possible substring if they are a palindrome
max = 1
for low in range(len(word)):                # Get lower bound for the word
    for high in range(low, len(word)):      # Get upper bound for the word
        substring = word[low:high+1]        # Create the substring
        # Check if the substring is a palindrome and compare its length
        if is_palindrome(substring) and max < len(substring):
            max = len(substring)

# Output
print(max)

