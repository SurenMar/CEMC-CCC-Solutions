# https://cemc.uwaterloo.ca/sites/default/files/documents/2025/2025CCCSrProblems.html

# Initialize variables
modulus = (10 ** 6) + 3
ans = 0
schedule = []   # Element format: [min_start, start, end]

# A function to update the schedule based on new updates
def update(new_update, s=None, t=None, i=None):
    pass

for _ in range(int(input())):
    line = list(map(int, input().split()))
    # Check type of update
    if line[0] == 'A':
        s = (line[1] + ans) % modulus
        t = (line[2] + ans) % modulus
        update('A', s=s, t=t)
    else:
        i = (line[1] + ans) % modulus
        update('B', i=i)
