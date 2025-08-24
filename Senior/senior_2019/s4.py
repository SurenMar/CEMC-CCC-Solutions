# https://cemc.uwaterloo.ca/sites/default/files/documents/2019/2019CCCSrProblems.html

num_dests, max_dests = map(int, input().split())
dest_scores = list(map(int, input().split()))

# Group the scores into groups of length max_dests
# There will be one group at the end with <max_dests length
# Arrange this arrangement by moving the last group aroun and seeing which
#   arrangement has the highest total score
