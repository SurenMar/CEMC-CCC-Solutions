# https://cemc.uwaterloo.ca/sites/default/files/documents/2015/2015CCCJrProblemSet.html

word = input()
# Create vowels list and a new word string
vowels = ['a', 'e', 'i', 'o', 'u']
new_word = ""

# Check every letter in inputted word
for letter in word:
    new_word += letter
    # Check if letter is a consonant
    if letter not in vowels:
        min = vowels[0]
        # For each vowel, set min vowel equal to current vowel if the distance
        #   from the current vowel to current letter is less than the that of 
        #   the min vowel to the current letter
        for vowel in vowels:
            if abs(ord(vowel) - ord(letter)) < \
                abs(ord(min) - ord(letter)):
                min = vowel
        new_word += min
        # Add z to new_word is the letter is z
        if letter == 'z':
            new_word += 'z'
        # Else, get the next consonant
        else:
            cons = chr(ord(letter)+1)
            while cons in vowels and not cons == 'z':
                cons = chr(ord(cons)+1)
            new_word += cons

# Output
print(new_word)