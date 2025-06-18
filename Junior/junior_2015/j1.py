# https://cemc.uwaterloo.ca/sites/default/files/documents/2015/2015CCCJrProblemSet.html

month = int(input())
day = int(input())

# Analyze month and day
if month < 2:
    output = "Before"
elif month > 2:
    output = "After"
elif day < 18:
    output = "Before"
elif day > 18:
    output = "After"
else:
    output = "Special"

# Output
print(output)