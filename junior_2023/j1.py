# https://cemc.uwaterloo.ca/sites/default/files/documents/2023/2023CCCJrProblemSet.html

p = int(input())
c = int(input())

if p > c:
    print(500 + p * 50 - c * 10)
else:
    print(p * 50 - c * 10)