# https://cemc.uwaterloo.ca/sites/default/files/documents/2025/2025CCCSrProblems.html

num_pens, num_colours, num_pictures = map(int, input().split())
num_pictures += 1

# Create a 2D pens array to store all the pens
pens = []
for _ in range(num_pens):
    colour, prettiness = map(int, input().split())
    pens.append([colour, prettiness])

# A function to read the next change, Q, update the corrosponding pen
def change_pen(pens):
    change_num, pen, change = map(int, input().split())
    if change_num == 1:
        pens[pen-1][0] = change
    else:
        pens[pen-1][1] = change

# Loop and create all needed pictures by determining max prettiness on each pic
prettiness = []
for i in range(num_pictures):
    # Loop through the up to date pens list and find the best pens
    best_pens = [0] * num_colours
    best_leftover = 0
    for pen in pens:
        if pen[1] > best_pens[pen[0]-1]:
            best_pens[pen[0]-1] = pen[1]
        elif pen[1] > best_leftover:
            best_leftover = pen[1]
    # Determine if an alteration is needed to get the max prettiness
    #   and append the max onto the prettiness list
    min_pen = min(best_pens)
    if min_pen > best_leftover:
        prettiness.append(sum(best_pens))
    else:
        prettiness.append(sum(best_pens) - min_pen + best_leftover)

    # Change the pen ONLY if we are not on the last picture
    if i+1 != num_pictures:
        change_pen(pens)

# Output
for pretty in prettiness:
    print(pretty)
