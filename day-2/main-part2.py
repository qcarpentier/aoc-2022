inputs_test = "day-2\inputs-test.txt"
inputs = "day-2\inputs.txt"

file = open(inputs, "r")
lines = file.readlines()

score = 0

for line in lines:
    turn = line.split()

    elf_hand = turn[0]
    our_hand = turn[1]

    if elf_hand == "A":
        elf_hand = "Rock"
    elif elf_hand == "B": 
        elf_hand = "Paper"
    elif elf_hand == "C": 
        elf_hand = "Scisor"

    # Lose
    if our_hand == "X":
        if elf_hand == "Rock":
            our_hand = "Scisor"
        elif elf_hand == "Paper":
            our_hand = "Rock"
        elif elf_hand == "Scisor":
            our_hand = "Paper"
    # Draw
    elif our_hand == "Y": 
        our_hand = elf_hand
    # Win
    elif our_hand == "Z": 
        if elf_hand == "Rock":
            our_hand = "Paper"
        elif elf_hand == "Paper":
            our_hand = "Scisor"
        elif elf_hand == "Scisor":
            our_hand = "Rock"

    # Calculate shape
    if our_hand == "Rock":
        score += 1
    elif our_hand == "Paper":
        score += 2
    elif our_hand == "Scisor":
        score += 3
    
    # Win
    if (our_hand == "Rock" and elf_hand == "Scisor") or \
        (our_hand == "Paper" and elf_hand == "Rock") or \
        (our_hand == "Scisor" and elf_hand == "Paper"):
        score += 6
    # Draw
    elif our_hand == elf_hand:
        score += 3
    # Lose
    else: 
        score += 0

print(score)