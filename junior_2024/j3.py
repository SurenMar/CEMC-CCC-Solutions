# https://cemc.uwaterloo.ca/sites/default/files/documents/2024/2024CCCJrProblemSet.html

scores = []
# Create list of all scores
for i in range(int(input())):
    scores.append(int(input()))

unique_scores = list(set(scores))       # remove duplicates from scores list
bronze = sorted(unique_scores)[-3]      # obtain the third highest score
num_bronze = scores.count(bronze)       # count the number of bronze scores

print(f"{bronze} {num_bronze}")