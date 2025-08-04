# https://cemc.uwaterloo.ca/sites/default/files/documents/2022/2022CCCSrProblems.html

num_friends = int(input())
friends = [tuple(map(int, input().split())) for _ in range(num_friends)]

# Find the max and min values of c
positions = [friend[0] for friend in friends]
high_c = max(positions)
low_c = min(positions)

# Computes value of f(c) = ∑max(0, |P - c| - D) * W
def dist_walked(c):
    f = 0
    for friend in friends:
        P = friend[0]
        W = friend[1]
        D = friend[2]
        f += max(0, abs(P - c) - D) * W
    return f

# Minimize the function f(c) = ∑max(0, |P - c| - D) * W
min_dist = dist_walked(high_c)
for c in range(low_c, high_c):
    min_dist = min(min_dist, dist_walked(c))

# Output
print(min_dist)

