# https://cemc.uwaterloo.ca/sites/default/files/documents/2019/2019CCCSrProblems.html

num_dests, max_dests = map(int, input().split())
dest_scores = list(map(int, input().split()))
leftover = num_dests % max_dests

# Calculate initial score
score = 0
groups = [max_dests] * (num_dests // max_dests)
groups.append(leftover) if leftover == 0 else None
for i, group in enumerate(groups):
    score += max(dest_scores[i * max_dests : (i+1) * max_dests])
# Output total score if there is no left over group
if leftover == 0:
    print(score)
    quit() 
# Shuffle the leftover group and find max score of each arrangement
else:
    high = num_dests
    low = num_dests - leftover - max_dests
    while low >= 0:
        score += max(dest_scores[low : high])
        low -= max_dests
        high -= max_dests

# Output
print(score)

