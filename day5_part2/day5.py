with open("ip.txt", "r") as f:
    lines = f.readlines()
    
for i in range(len(lines)):
    if lines[i] == "\n":
        crates_part = lines[:i]
        moves_part = lines[i+1:]

crate_nums = crates_part[-1].split()
num_crates = len(crate_nums)

piles = [line[:-1] for line in crates_part[:-1]]
crates_dict = {}
for row in piles:
    i = 0
    crate_num = 1
    while i < (len(row)):
        if row[i] != "[":
            # skip
            i += 4
        else:
            if crate_num in crates_dict:
                crates_dict[crate_num].append(row[i + 1 : i + 2])
    
            else:
                crates_dict[crate_num] = [row[i + 1 : i + 2]]
            # i =
            i += 4

        crate_num += 1
        
for crate in crates_dict:
    crates_dict[crate] = crates_dict[crate][::-1]


moves = []
for i in range(len(moves_part)):
    moves_part[i] = moves_part[i].strip()
    n = int(moves_part[i][ moves_part[i].find("move") + 5: moves_part[i].find("from") ])
    c1 = int(moves_part[i][ moves_part[i].find("from") + 5: moves_part[i].find("to") ])
    c2 = int(moves_part[i][ moves_part[i].find("to") + 3 : ])
    moves.append( (n, c1, c2) )

for move in moves:
    (n, c1, c2) = move
    
    crates_picked = []
    for i in range(n):
        crate_picked = crates_dict[c1].pop()
        crates_picked.append(crate_picked)
    crates_picked = crates_picked[::-1]
    crates_dict[c2] += crates_picked
    

for k in (sorted(crates_dict)):
    # print(f"{k} -> {crates_dict[k]}")
    print(crates_dict[k][-1], end="")
print()



