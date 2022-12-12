inputs_test = "day-1\inputs-test.txt"
inputs = "day-1\inputs.txt"

file = open(inputs, "r")
lines = file.readlines()
sum_of_calories = 0
total_calories = 0
elves = []

# For each line
for line in lines:
    # Sum the calories if it's the same elf
    if (line != "\n"): 
        sum_of_calories = sum_of_calories + int(line)
    # If it's not the same elf anymore, add the sum of calories
    # to elves and reset the sum
    else:
        elves.append(sum_of_calories)
        sum_of_calories = 0

# Last elf
elves.append(sum_of_calories)

# Sort asc per elf
elves.sort()

# Sum the top three elves
for elf in elves[-3:]:
    total_calories += elf

print(total_calories)
