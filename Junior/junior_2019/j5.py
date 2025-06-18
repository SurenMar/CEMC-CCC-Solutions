# https://cemc.uwaterloo.ca/sites/default/files/documents/2019/2019CCCJrProblemSet.html

rule1 = input().split()
rule2 = input().split()
rule3 = input().split()
steps, start, end = input().split()
steps = int(steps)

# Function that applies any given rule/sub to a string at an index
def sub(string, rule, index):
    # Check if a sub at index is valid
    if string[index:index+len(rule[0])] != rule[0]:
        return False
    # Copy all elements into a new string up to index of substitution
    new_string = string[:index]
    # Add the sub rule to the string
    new_string += rule[1]
    # Add all elements needed to be copied after the sub rule
    new_string += string[index+len(rule[0]):]
    return new_string   # Return new string

# Recursive function that outputs a possible process to convert a string
def convert(string, process):
    # Check if final string has been reached with required amount of steps
    if string == end and steps == len(process):
        return process
    # Check if required steps has been passed
    elif steps <= len(process):
        return False
    else:
        # Apply rule 1
        for i in range(len(string)):
            # Apply rule 1 at given index
            new_string1 = sub(string, rule1, i)
            # Check if i was a valid index for the given rule
            if new_string1:
                # Call recursive function with new sub appended onto processes
                new_process = process + [[1, i+1, new_string1]]
                final = convert(new_string1, new_process)
                # If returned value is not false, then it is a valid process
                if final:
                    return final
                
        # Apply rule 2
        for i in range(len(string)):
            # Apply rule 2 at given index
            new_string2 = sub(string, rule2, i)
            # Check if i was a valid index for the given rule
            if new_string2:
                # Call recursive function with new sub appended onto processes
                new_process = process + [[2, i+1, new_string2]]
                final = convert(new_string2, new_process)
                if final:
                    return final
                
        # Apply rule 3
        for i in range(len(string)):
            # Apply rule 3 at given index
            new_string3 = sub(string, rule3, i)
            # Check if i was a valid index for the given rule
            if new_string3:
                # Call recursive function with new sub appended onto processes
                new_process = process + [[3, i+1, new_string3]]
                final = convert(new_string3, new_process)
                # If returned value is not false, then it is a valid process
                if final:
                    return final

# Output
processes = convert(start, [])
for process in processes:
    print(f"{process[0]} {process[1]} {process[2]}")
        
            