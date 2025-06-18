# https://cemc.uwaterloo.ca/sites/default/files/documents/2019/2019CCCJrProblemSet.html

messages = []   # variable to hold all decoded messages
for _ in range(int(input())):
    msg = input().split()
    messages.append(msg[1] * int(msg[0]))   # creates appends decoded string
    
# output
for message in messages:
    print(message)