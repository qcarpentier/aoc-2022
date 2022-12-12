inputs_test = "day-4\inputs-test.txt"
inputs = "day-4\inputs.txt"

file = open(inputs, "r")
lines = file.readlines()

sections = []

score = 0

def check_overlap():
    for i in range(area_minimum_elf_1, area_maximum_elf_1 + 1):
        for j in range(area_minimum_elf_2, area_maximum_elf_2 + 1):
            if i == j:
                return 1

    return 0

for line in lines:
    # ['6-6', '4-6']
    sections = line.strip().split(",")

    areas_elf_1 = sections[0]
    areas_elf_2 = sections[1]

    area_minimum_elf_1 = int(areas_elf_1.split("-")[0])
    area_maximum_elf_1 = int(areas_elf_1.split("-")[1])
    area_minimum_elf_2 = int(areas_elf_2.split("-")[0])
    area_maximum_elf_2 = int(areas_elf_2.split("-")[1])

    score += check_overlap()

print(score)