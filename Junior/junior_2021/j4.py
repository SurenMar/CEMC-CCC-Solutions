# https://cemc.uwaterloo.ca/sites/default/files/documents/2021/2021CCCJrProblemSet.html

# create number representation of the books for easy work arounds
books_num = []
for book in input():
    if book == 'L':
        books_num.append(3)
    elif book == 'M':
        books_num.append(2)
    else:
        books_num.append(1)

# function which swaps two elements
def swap(i1, i2, books_num):
    temp = books_num[i1]
    books_num[i1] = books_num[i2]
    books_num[i2] = temp

# function which returns the index of the rightmost book inside books list
#   with the given size
def find_size(needed_size, books_num):
    index = len(books_num) - 1
    while index >= 0 and books_num[index] != needed_size:
        index -= 1
    return index    # returns -1 if no such book is found


needed_size = max(books_num)    # stores the current size which is needed
index = 0                       # current index of the books_num list
swaps = 0                       # number of swaps done

# loop through entirety of books_num list
while index < len(books_num):
    size = books_num[index]     # get size of current book
    if size != needed_size:     # check if current size if the one we are looking for
        i1 = index
        i2 = find_size(needed_size, books_num) # index of right most book with the needed size
        
        # check if needed size doesnt exist or its behind (left of) the current book
        if i2 == -1 or i2 < index:
            needed_size -= 1            # decrease needed size (since we converted books to numbers)
            continue                    # dont increment index
        else:
            swap(i1, i2, books_num)     # swap if the size DOES exist
            swaps += 1
    index += 1
    
# output
print(swaps)
            