# https://cemc.uwaterloo.ca/sites/default/files/documents/2020/2020CCCJrProblemSet.html

num_points = int(input())
# read first point to use as reference
init_point = list(map(int, input().split(',')))
# max and min values for the frame
top = init_point[1]
right = init_point[0]
bottom = init_point[1]
left = init_point[0]
# read points
for _ in range(num_points - 1):
    point = list(map(int, input().split(',')))
    # check x coord
    if point[0] > right:
        right = point[0]
    elif point[0] < left:
        left = point[0]
    # check y coord
    if point[1] > top:
        top = point[1]
    elif point[1] < bottom:
        bottom = point[1]
        
# output
# note the +/-1 adjustment used for the frame
print(f"{left - 1},{bottom - 1}")
print(f"{right + 1},{top + 1}")
    
    

    
