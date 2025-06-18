# https://cemc.uwaterloo.ca/sites/default/files/documents/2016/2016CCCJrProblemSet.html

question = input()
pairs = int(input())
# Read and sort the speeds of each citizen
n1 = sorted(list(map(int, input().split())))
n2 = sorted(list(map(int, input().split())))

# A function that merges the two lists n1 and n2
def merge(n1, n2):
    n = []
    while n1 or n2:
        if not n1 or (n2 and n1[0] > n2[0]): 
            n.append(n2.pop(0))
        else:
            n.append(n1.pop(0))
    return n

# Sums the max of each pair in lists n1 and n2. 
# Assumes they are of the same length
def pair_sum(n1, n2):
    sum = 0
    for i in range(pairs):
        sum += max(n1[i], n2[i])
    return sum

# If question numebr is 1, find its pair sum
if question == '1':
    print(pair_sum(n1, n2))
# If question number is 2, find the sum of the second half of the merged list
# That is, the the sum of the largest numbers in the merged list
else:
    print(sum(merge(n1[:], n2[:])[-pairs:]))