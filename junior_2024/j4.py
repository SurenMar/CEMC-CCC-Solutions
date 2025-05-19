# https://cemc.uwaterloo.ca/sites/default/files/documents/2024/2024CCCJrProblemSet.html

expectations = input()
reality = input()

# check strings until first letter difference
i = 0
while expectations[i] == reality[i]:
   i += 1

# if lengths are same, then there must be no quiet letter
if len(expectations) == len(reality):
    print(f"{expectations[i]} {reality[i]}")
    print("-")
else:
    # check expectation word until different letter is found
    j = i
    while expectations[j] == expectations[i]:
        j += 1
        
    # if the first different letter matches the one from the reality word
    #   at the stopping point (from the first while loop), then that original
    #   different letter must be the quiet letter since all instances of it
    #   are missing in the reality word
    if expectations[j] == reality[i]:
        quiet = expectations[i]
        while i < len(reality):
            # if current expectations letter is the quiet letter, skip past it
            #   by not incrementing the index for reality word
            if expectations[j] == quiet:
                j += 1
            # if theres a letter difference which is not the quiet letter, then
            #   it must be the silly letter
            elif expectations[j] != reality[i] and expectations[j] != quiet:
                print(f"{expectations[j]} {reality[i]}")
                print(quiet)
                break
            # increment both word indexes
            else:
                j += 1
                i += 1
    # if above if statement is false, then the letter difference must mean
    #   it was caused by the silly letter
    # note: we know there is a quiet letter since lengths arent the same
    else:
        silly = reality[i]
        print(f"{expectations[i]} {silly}")

        # check for first character difference that isnt caused by the
        #   silly letter => it was caused by the quiet letter
        while i < len(reality):
            if expectations[i] != reality[i] and reality[i] != silly:
                break
            i += 1
        print(expectations[i])
        
