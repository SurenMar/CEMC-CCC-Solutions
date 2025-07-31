# https://cemc.uwaterloo.ca/sites/default/files/documents/2022/2022CCCSrProblems.html

num_points, circ = map(int, input().split())
points = list(sorted(map(int, input().split())))
diameter = circ / 2

# Go around the circle finding good triplets
count = 0
# Pick first point
for i1 in range(num_points):
    # Pick second point
    for i2 in range(i1, num_points):
        # Continue if both points are the same
        if points[i1] == points[i2]:
            continue
        # Break if the second point is past the opposite of the first point
        elif points[i1] + diameter <= points[i2]:
            break
        # Pick second point
        for i3 in range(i2, num_points):
            # Continue if third point is the same as first point
            if points[i3] == points[i1]:
                continue
            # Break if the third point is past the opposite of the second point
            elif points[i2] + diameter <= points[i3]:
                break
            # Increase counter if middle point is enclosed by the 3 points
            elif points[i3] > points[i1] + diameter and \
               points[i3] < points[i2] + diameter:
                count += 1

# Output
print(count)




