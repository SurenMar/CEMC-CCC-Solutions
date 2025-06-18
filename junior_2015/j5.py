# https://cemc.uwaterloo.ca/sites/default/files/documents/2015/2015CCCJrProblemSet.html

num_pies = int(input())
num_people = int(input())

# A partition function that counts the number of partitions for pcs pieces
#   among ppl people with a lower bound of min_pcs
def count_ways(ppl, pcs, min_pcs):
    # Base case 1: There are no people left
    if ppl == 0:
        # If there are also no pieces left, partition is successful
        if pcs == 0:
            return 1
        else:
            return 0
    # Base case 2: If pieces are already less than the minimum number of
    #   of pieces required for each person, then theres no reason continuing
    elif pcs < ppl * min_pcs:
        return 0
    # Recursive case: Find the sum of all partitions with the different
    #   possible min_pcs distributed
    else:
        sum = 0
        for i in range(min_pcs, pcs + 1):
            sum += count_ways(ppl - 1, pcs - i, i)
        return sum

# Output
print(count_ways(num_people, num_pies, 1))