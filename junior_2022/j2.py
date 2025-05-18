count = 0
n = int(input())
for i in range(n):
    # increase count only if points is greater than 40
    if 5 * int(input()) - 3 * int(input()) > 40:
        count += 1
 
# check if all n players got above 40 points
if count < n:
    print(f"{count}")
else:
    print(f"{count}+")