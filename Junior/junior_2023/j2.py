# https://cemc.uwaterloo.ca/sites/default/files/documents/2023/2023CCCJrProblemSet.html

# Peppers dictionary using first letters to distinguish between peppers since
#   all first letters are distinct
peppers = {
    'P': 1500,
    'M': 6000,
    'S': 15500,
    'C': 40000,
    'T': 75000,
    'H': 125000
}

total = 0
for i in range(int(input())):
    total += peppers[input()[0]]    # Access dictionary using first character
                                    #   of inputted name
print(total)