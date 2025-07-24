# https://cemc.uwaterloo.ca/sites/default/files/documents/2022/2022CCCSrProblems.html

# Read students who must be in same group
same_group1 = []
same_group2 = []
for i in range(int(input())):
    pair = input().split()
    same_group1.append(pair[0])
    same_group2.append(pair[1])

# Read students who must be in different groups
diff_group1 = []
diff_group2 = []
for i in range(int(input())):
    pair = input().split()
    diff_group1.append(pair[0])
    diff_group2.append(pair[1])

# Read groups and count violations
violations = 0
for i in range(int(input())):
    group = input().split()
    
    # Loop through group and see if any violations are made
    for j in [0, 1, 2]:
        # Check if current student in group must be grouped with a certain student
        if group[j] in same_group1:
            index = same_group1.index(group[j])     # Get index
            if same_group2[index] not in group:     # Check if students pair IS NOT in group
                violations += 1
        # Same as above if statement
        elif group[j] in same_group2:
            index = same_group2.index(group[j])     # Get index
            if same_group1[index] not in group:     # Check if students pair IS NOT in group
                violations += 1
        
        # Check if current student in group must not be grouped with a certain student
        if group[j] in diff_group1:
            index = diff_group1.index(group[j])     # Get index
            if diff_group2[index] in group:         # Check if students pair IS in group
                violations += 1
        # Same as above if statement
        elif group[j] in diff_group2:
            index = diff_group2.index(group[j])     # Get index
            if diff_group1[index] in group:         # Check if students pair IS in group
                violations += 1

violations //= 2    # Half violations to account for double counting since if
                    #   one student commits a violations, their partners
                    #   violation will also be counted (as per the code), 
                    #   making it 2 total violations instead 1
# Output
print(violations)