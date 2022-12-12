inputs_test = "day-4\inputs-test.txt"
inputs = "day-4\inputs.txt"

file = open(inputs, "r")
lines = file.readlines()

sections = []

score = 0

for line in lines:
    # ['6-6', '4-6']
    sections = line.strip().split(",")

    areas_elf_1 = sections[0]
    areas_elf_2 = sections[1]

    area_minimum_elf_1 = int(areas_elf_1.split("-")[0])
    area_maximum_elf_1 = int(areas_elf_1.split("-")[1])
    area_minimum_elf_2 = int(areas_elf_2.split("-")[0])
    area_maximum_elf_2 = int(areas_elf_2.split("-")[1])

    # Area elf 1 fully contained in area elf 2
    # ['6-6', '4-6']
    if  area_minimum_elf_1 >= area_minimum_elf_2 and \
        area_maximum_elf_1 <= area_maximum_elf_2:
        score += 1
       
    # Area elf 2 fully contained in area elf 1
    # ['2-8', '3-7']
    elif area_minimum_elf_2 >= area_minimum_elf_1 and \
         area_maximum_elf_2 <= area_maximum_elf_1:
        score += 1

print(score)