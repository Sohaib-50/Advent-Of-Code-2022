with open("inp.txt") as f:
    input_str = f.read()

input_str = input_str.split("\n\n")
input_str = [x.split("\n") for x in input_str]

max_1 = 0
max_2 = 0
max_3 = 0
for elf in input_str:
    current_calories = 0
    for food in elf:
        current_calories += int(food)
    
    if current_calories > max_1:
        max_3 = max_2
        max_2 = max_1
        max_1 = current_calories
    elif current_calories > max_2:
        max_3 = max_2
        max_2 = current_calories
    elif current_calories > max_3:
        max_3 = current_calories

print(sum([max_1, max_2, max_3]))
