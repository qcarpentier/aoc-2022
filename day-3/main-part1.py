inputs_test = "day-3\inputs-test.txt"
inputs = "day-3\inputs.txt"

file = open(inputs, "r")
lines = file.readlines()

score = 0

lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
uppercase_alphabet = "abcdefghijklmnopqrstuvwxyz".upper()

for line in lines:
    char_numbers = len(line)

    # Divide the line in two parts (// -> floor division)
    # set() -> unique character
    firstpart_rucksack = set(line[:char_numbers//2])
    secondpart_rucksack = set(line[char_numbers//2:])

    # Find common letter with intersection(), then join() it into a string
    common_letter = ''.join(firstpart_rucksack.intersection(secondpart_rucksack))

    # Calculate the priority by finding the letter priority number
    if (lowercase_alphabet.find(common_letter) != -1):
        priority = lowercase_alphabet.find(common_letter)
    else:
        priority = uppercase_alphabet.find(common_letter) + 26

    score += priority + 1

print(score)