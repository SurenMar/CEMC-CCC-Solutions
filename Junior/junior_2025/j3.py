# https://cemc.uwaterloo.ca/sites/default/files/documents/2025/2025CCCJrProblemSet.html

n = int(input())

# list to store the new codes
new_codes = []

for i in range(n):
    code = input()
    new_code = ''       # start building the new code
    sum = 0             # running total for integers
    num = 0             # current integer being processed
    sign = 1            # current sign of num
    
    for c in range(len(code)):
        if code[c].isalpha():       # check if current char is a letter
            # add num to running total. if there was none, it adds 0
            sum += sign * num
            # reset values
            num = 0
            sign = 1
            if code[c].isupper():
                new_code += code[c]     # keep uppercase letters
        elif code[c].isnumeric():
            # if digit, build the current integer being processed
            num = num * 10 + int(code[c])
        elif code[c] == '-':
            # if encounter a negative sign, perform same steps as 
            #   when a letter is encountered, except keep the sign negative
            sum += sign * num
            num = 0
            sign = -1
    # add any remaining integer and attach sum to new_code
    sum += sign * num
    new_code += str(sum)
    new_codes.append(new_code)

for new_code in new_codes:
    print(new_code)