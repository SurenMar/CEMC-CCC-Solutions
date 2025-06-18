# https://cemc.uwaterloo.ca/sites/default/files/documents/2020/2020CCCJrProblemSet.html

text = input()
string = input()

# helper function which shifts a string
def shift(string):
    shifted_string = string[1:]     # save all but the first letter to a variable
    shifted_string += string[0]     # add the first letter to the very end
    return shifted_string

# check if a cyclic shift of string is in text
output = 'no'
# this checks all shifts since a string of length n has n shifts
for _ in range(len(string)):
    if string in text:          # check if string is in text
        output = 'yes'  
        break
    string = shift(string)      # shift string
    
# output
print(output)
    