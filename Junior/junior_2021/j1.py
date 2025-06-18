# https://cemc.uwaterloo.ca/sites/default/files/documents/2021/2021CCCJrProblemSet.html

pressure = int(input()) * 5 - 400
print(pressure)
if pressure > 100:
    print('-1')
elif pressure < 100:
    print('1')
else:
    print('0')
