# https://cemc.uwaterloo.ca/sites/default/files/documents/2022/2022CCCSrProblems.html

N, M, K = map(int, input().split())

# Initialize variables
max_notes = []
min_notes = []
solutions = 0

# Function to check if a sequence is good
def is_good(seq):
    # Check if all adjacent differences are at most 1
    for i in range(len(seq) - 1):
        if abs(seq[i] - seq[i + 1]) > 1:
            return False
    # Check if max and min notes match input
    if max(seq) != max_notes[0] or min(seq) != min_notes[0]:
        return False
    return True

# Generate all possible sequences
def generate_sequences(curr_seq, notes_left, prev_note):
    global solutions
    if notes_left == 0:
        if len(curr_seq) == N and is_good(curr_seq):
            solutions += 1
        return
    
    # Try notes from min to max
    for note in range(min_notes[0], max_notes[0] + 1):
        # Check if note can be used (adjacent difference <= 1)
        if prev_note is None or abs(note - prev_note) <= 1:
            curr_seq.append(note)
            generate_sequences(curr_seq, notes_left - 1, note)
            curr_seq.pop()

# Read max and min notes
for i in range(M):
    max_notes.append(int(input()))
for i in range(M):
    min_notes.append(int(input()))

# Generate sequences and count good ones
generate_sequences([], N, None)

# Output result modulo 10^9 + 7
print(solutions % (10**9 + 7))