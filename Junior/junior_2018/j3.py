# https://cemc.uwaterloo.ca/sites/default/files/documents/2018/2018CCCJrProblemSet.html

distances = list(map(int, input().split()))

# Create x-axis with origin being the first city
axis = [0]
for dist in distances:
    axis.append(axis[-1] + dist)

# For each city, print the distance from every city in axis to the given city
for city in range(5):
    for dist in axis:
        print(abs(axis[city] - dist), end=' ')
    print()
    
# Note, I am aware a whitespace is included at the end of each line.
#   I did not bother to fix this detail because these solutions are
#   mearly for a generall aid and guide to solving the problem.