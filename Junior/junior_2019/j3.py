# https://cemc.uwaterloo.ca/sites/default/files/documents/2019/2019CCCJrProblemSet.html

encoded_msgs = []   # variable to keep track of all encoded messages
for _ in range(int(input())):
    message = input()       # read the message to encode
    encoded_msg = ''        # current encoded message
    symbol = message[0]     # current symbol were counting
    symbol_count = 0        # counter for current symbol
    
    # count each character in current message
    for char in message:
        # check if symbol needs to be changed
        if char != symbol:
            # append first 'block' of encoding (notice whitespace at end)
            encoded_msg += f"{symbol_count} {symbol} "
            symbol = char       # change symbol
            symbol_count = 1    # reset count
        # increment count if symbol has not changed
        else:
            symbol_count += 1
    
    # append last block of encoding (notice no whitespace at end)
    encoded_msg += f"{symbol_count} {symbol}"
    # append current encoded message to all the encoded messages
    encoded_msgs.append(encoded_msg)
    
# output
for encoded_msg in encoded_msgs:
    print(encoded_msg)
        