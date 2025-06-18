# https://cemc.uwaterloo.ca/sites/default/files/documents/2021/2021CCCJrProblemSet.html

max = 0     # contains the highest bid
name = ''   # contains name of highest bidder
for i in range(int(input())):
    bidder = input()
    bid = int(input())
    if max < bid:
        max = bid
        name = bidder   # set name only if the current bid strictly greater 
                        #   is higher than max

# output
print(name)
        
