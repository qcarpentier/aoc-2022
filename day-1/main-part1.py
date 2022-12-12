inputs_test = "day-1\inputs-test.txt"
inputs = "day-1\inputs.txt"

file = open(inputs, "r")
lines = file.readlines()
sum = 0
max = 0

for line in lines:
    if (line != "\n"): 
        sum = sum + int(line)

        if (sum >= max):
            max = sum
    else:
        sum = 0

print(max)