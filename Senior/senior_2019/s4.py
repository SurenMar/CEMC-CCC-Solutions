# https://cemc.uwaterloo.ca/sites/default/files/documents/2019/2019CCCSrProblems.html

num_dests, max_dests = map(int, input().split())
dest_scores = list(map(int, input().split()))

leftover = num_dests % max_dests

# Group the scores into groups of length max_dests
# There will be one group at the end with <max_dests length
# Arrange this arrangement by moving the last group aroun and seeing which
#   arrangement has the highest total score

# (1 2 3) (4 5 6) (7 8)
# (1 2 3) (4 5) (6 7 8)
# (1 2) (3 4 5) (6 7 8)

# Caclulates score of a specific group in lst
def calc_score(lst, start, group_len):
    i = start
    score = 0
    while i < start + group_len:
        score += lst[i]
    return score

# Add the remaining group and calculate current total score
score = 0
high = num_dests - 1
low = num_dests - leftover - max_dests
# Output total score if there is no left over group
if len(leftover == 0):
    print(score)
    quit() 
# Shuffle the leftover group and find max score of each arrangement
else:
    high = num_dests - 1
    low = num_dests - leftover - max_dests
    while True:
        # Calculate current score

        score = max(score, )

