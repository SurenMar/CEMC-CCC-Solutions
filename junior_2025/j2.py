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
