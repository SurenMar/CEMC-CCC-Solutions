# https://cemc.uwaterloo.ca/sites/default/files/documents/2024/2024CCCJrProblemSet.html

d = int(input())    # Dusa's size
y = int(input())    # First yobis size

# Eats yobis until it encounters one larger than it
while d > y:
    d += y
    y = int(input())

print(d)


    
