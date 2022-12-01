
with open("inp.txt") as f:
    input_str = f.read()

input_str = input_str.split("\n\n")
input_str = [x.split("\n") for x in input_str]

max_calories = 0
for elf in input_str:
    current_calories = 0
    for food in elf:
        current_calories += int(food)
    max_calories = max(max_calories, current_calories)

print(max_calories)