with open("ip.txt", "r") as f:
    rucksacks = []
    for line in f:
        rucksacks.append(line.strip())
    
priority_sum = 0

for rucksack in rucksacks:
    rucksack1 = rucksack[:len(rucksack)//2]
    rucksack2 = set(rucksack[len(rucksack)//2:])
    
    for item in rucksack1:
        if item in rucksack2:
            if item.isupper():
                priority_sum += ord(item) - 65 + 27
            else:
                priority_sum += ord(item) - 97 + 1
            break

print(priority_sum)