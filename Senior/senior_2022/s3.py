# https://cemc.uwaterloo.ca/sites/default/files/documents/2022/2022CCCSrProblems.html

num_notes, max_pitch, desired_samples = map(int, input().split())

# Subtract 1-length good samples
desired_samples -= num_notes

# Impossible if too few or too many
if desired_samples < 0 or desired_samples > (num_notes * (num_notes - 1)) // 2:
    print(-1)
    exit()

sequence = [1]
next_note = 2  # Next unique value to use

for i in range(1, num_notes):
    # Adding a new unique value here adds i new good samples
    if desired_samples >= i and next_note <= max_pitch:
        sequence.append(next_note)
        next_note += 1
        desired_samples -= i
    else:
        # Back-reference to a value K positions before to add exactly K good samples
        if desired_samples > 0:
            sequence.append(sequence[i - desired_samples - 1])
            desired_samples = 0
        else:
            sequence.append(sequence[-1])  # Just repeat to avoid new good samples

# Final check
if desired_samples == 0:
    print(" ".join(map(str, sequence)))
else:
    print(-1)
