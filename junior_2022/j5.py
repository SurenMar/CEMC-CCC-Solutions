# https://cemc.uwaterloo.ca/sites/default/files/documents/2022/2022CCCJrProblemSet.html

n = int(input())
trees = int(input())

# create a 2D list to mark tree positions
yard = [[0] * n for _ in range(n)]

# mark all trees on the yard
for _ in range(trees):
    r, c = map(int, input().split())
    yard[r][c] = 1

# build 2D prefix sum grid
prefix = [[0] * n for _ in range(n)]
for i in range(1, n):
    for j in range(1, n):
        # calculate current prefix sum entry by moving in both up and 
        #   left directions from current position
        prefix[i][j] = yard[i][j] + prefix[i - 1][j] + prefix[i][j - 1] - \
            prefix[i - 1][j - 1]

# helper function to check if a square of given size fits without trees
def can_place(size):
    for i in range(1, n - size + 1):
        for j in range(1, n - size + 1):
            r1, c1 = i, j
            r2, c2 = i + size - 1, j + size - 1
            # calculate number of trees in current square using prefix 
            #   sum difference
            tree_count = prefix[r2][c2] - prefix[r1 - 1][c2] - \
                prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1]
            # note we add prefix[r1 - 1][c1 - 1] back because it got
            #   subtracted twice in the above arithmetic
            if tree_count == 0:
                return True
    return False

# binary search grid for the largest square size
low = 1
high = n
ans = 0

while low <= high:
    mid = (low + high) // 2
    if can_place(mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

# output
print(ans)
