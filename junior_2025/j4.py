# https://cemc.uwaterloo.ca/sites/default/files/documents/2025/2025CCCJrProblemSet.html

s_counter = [0, 0]      # counter for each s: one's before a P and ones after
current_s = 0           # index of s_counter were currently updating
p_counter = 0           # number of P's currently seen
max_s = 1               # the max sunshines possible

for i in range(int(input())):
    data = input()
    
    # second P seen in current block
    if data == 'P' and p_counter == 1:
        max_s = max(max_s, sum(s_counter) + 1)  # finds new max, +1 is to account for the P
        s_counter[0] = 0    # reset 'before P' counter
        p_counter = 0       # reset P counter
        current_s = 0       # start counting S's before next P
    # first P seen in current block
    elif data == 'P':
        max_s = max(max_s, sum(s_counter) + 1)
        p_counter += 1      # mark that we've seen a P in current block
        s_counter[1] = 0    # reset 'after P' counter
        current_s = 1       # start counting S's after current P
    elif data == 'S':
        s_counter[current_s] += 1   # increment S's seen in current block
        
max_s = max(max_s, sum(s_counter) + 1) # Evaluate any remaining sequences
print(max_s)
    