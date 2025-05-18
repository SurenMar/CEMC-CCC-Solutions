instructions = input()

for i in range(len(instructions)):
    if instructions[i].isalpha():
        print(instructions[i], end='')  # print letter without newline
    elif instructions[i] == '+':
        print(' tighten ', end='')      # print ' tighten ' without newline
    elif instructions[i] == '-':
        print(' loosen ', end='')       # print ' loosen ' without newline
    else:
        print(instructions[i])          # print number with newline

