inputs_test = "day-5\inputs-test.txt"
inputs = "day-5\inputs.txt"

file = open(inputs_test, "r")
lines = file.read()

# Split crates and movements
crates, movements = lines.split("\n\n")
crates = crates.splitlines()
movements = movements.splitlines()

# Get number of stacks (last line, get the max)
number_of_stacks = int(max(crates[-1].split()))

horizontal_stacks = []
vertical_stacks = []

top_crates = ""

# Get horizontal stacks
for crate in crates:
    line_elements = []
    for i in range(2, number_of_stacks * 4, 4):
        line_elements.append(crate[i - 1])

    # [[' ', 'D', ' '], ['N', 'C', ' '], ['Z', 'M', 'P'], ['1', '2', '3']]
    horizontal_stacks.append(line_elements)

# Get vertical stacks
for stack_number in range(number_of_stacks):
    row_elements = []
    for crate in range(number_of_stacks):
        actual_crate = horizontal_stacks[crate][stack_number]
        if actual_crate != " ":
            row_elements.append(actual_crate)
    
    # [['N', 'Z'], ['D', 'C', 'M'], ['P']]
    vertical_stacks.append(row_elements)

for move in movements:
    move_count = int(move.split()[1])
    stack_from = int(move.split()[3]) - 1
    stack_to = int(move.split()[5]) - 1

    for i in range(move_count):
        # Insert the crane (the first element of the stack_from) as the element of the stack_to in same order
        vertical_stacks[stack_to].insert(i, vertical_stacks[stack_from][0])
        # Delete the inserted crane from its previous position
        del vertical_stacks[stack_from][0]

        # [['M'], ['C'], ['D', 'N', 'Z', 'P']]

# Get top crates
for crate in vertical_stacks:
    top_crates += crate[0]

print(top_crates)