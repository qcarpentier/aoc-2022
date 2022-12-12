inputs_test = "day-3\inputs-test.txt"
inputs = "day-3\inputs.txt"

file = open(inputs, "r")
lines = file.readlines()

score = 0
count = 0

elf_rucksacks = []

lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
uppercase_alphabet = "abcdefghijklmnopqrstuvwxyz".upper()

for line in lines:
    elf_rucksacks.append(line)
    count += 1

    if count >= 3:
        # For each rucksack, find unique values with set()
        first_rucksack = set(elf_rucksacks[0])
        second_rucksack = set(elf_rucksacks[1])
        third_rucksack = set(elf_rucksacks[2])

        # Find common value with & on set() and store it into a string with join()
        common_item = "".join(first_rucksack & second_rucksack & third_rucksack).strip()

        # Calculate the priority by finding the letter priority number
        if (lowercase_alphabet.find(common_item) != -1):
            priority = lowercase_alphabet.find(common_item)
        else:
            priority = uppercase_alphabet.find(common_item) + 26

        score += priority + 1

        # Reset variables
        elf_rucksacks = []
        group_rucksacks = ""
        count = 0

print(score)