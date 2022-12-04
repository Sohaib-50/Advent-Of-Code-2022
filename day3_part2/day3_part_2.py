with open("ip.txt", "r") as f:
    rucksacks = []
    for line in f:
        rucksacks.append(line.strip())

rucksack_groups = []
for i in range(0, len(rucksacks) - 2, 3):
    rucksack_groups.append(rucksacks[i:i+3])

print(rucksack_groups)
    
priority_sum = 0

for rucksack_group in rucksack_groups:
    rucksack1 = rucksack_group[0]
    rucksack2 = set(rucksack_group[1])
    rucksack3 = set(rucksack_group[2])
    
    for item in rucksack1:
        if item in rucksack2 and item in rucksack3:
            if item.isupper():
                priority_sum += ord(item) - 65 + 27
            else:
                priority_sum += ord(item) - 97 + 1
            break

print(priority_sum)