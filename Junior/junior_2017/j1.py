# https://cemc.uwaterloo.ca/sites/default/files/documents/2017/2017CCCJrProblemSet.html

x = int(input())
y = int(input())

# Check negativity and positivity
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)