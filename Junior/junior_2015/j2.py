# https://cemc.uwaterloo.ca/sites/default/files/documents/2015/2015CCCJrProblemSet.html

text = input()

# Count all happys and sads
sad = text.count(":-(")
happy = text.count(":-)")

# Output
if happy > sad:
    print("happy")
elif happy < sad:
    print("sad")
else:
    print("unsure")