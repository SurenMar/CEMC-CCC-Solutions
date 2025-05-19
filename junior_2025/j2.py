# https://cemc.uwaterloo.ca/sites/default/files/documents/2025/2025CCCJrProblemSet.html

d = int(input())
e = int(input())

for i in range(e):
    sign = input()
    q = int(input())
    
    # perform operation to total donuts depending on sign
    if sign == '+':
        d += q
    else:
        d -= q
        
print(d)
