# https://cemc.uwaterloo.ca/sites/default/files/documents/2018/2018CCCSrProblems.html

num_villages = int(input())
villages = [int(input()) for _ in range(num_villages)]
villages = sorted(villages)

def avg(a, b):
    return (a + b) / 2

# Calculate neighbourhood lengths of villages 2 to n-1
v = 1
min_dist = float('inf')
while v < num_villages - 1:
    cur_dist = \
        avg(villages[v+1], villages[v]) - avg(villages[v], villages[v-1])
    min_dist = min(min_dist, cur_dist)
    v += 1

# Output
print(min_dist)
