# https://cemc.uwaterloo.ca/sites/default/files/documents/2020/2020CCCJrProblemSet.html

cap = int(input())
infected = int(input())
spread = int(input())

day = 0     # counter for days
while infected <= cap:
    # multiply currently infected people by the amount that they pass 
    #   it on to (spread) and add it on to running total
    infected += (infected * spread)
    day += 1

# output
print(day)