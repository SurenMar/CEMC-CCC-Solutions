# https://cemc.uwaterloo.ca/sites/default/files/documents/2019/2019CCCSrProblems.html

sums = [2 * int(input()) for _ in range(int(input()))]

# Determines whether n is prime (use optimized version for high numbers)
def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# Loop through each sum and find two primes
for sum in sums:
    i = 2
    while i <= sum // 2:
        if is_prime(i) and is_prime(sum - i):
            # Output
            print(i, sum - i)
            break
        i += 1
