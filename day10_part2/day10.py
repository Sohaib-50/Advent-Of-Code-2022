instructions = []
with open("ip.txt") as f:
    for line in f:
        instructions.append(line.strip())

cycles = 1
x = 1
CRT = [[" " for i in range(40)] for j in range(6)]  # 40 wide 6 high
ans = 0
i = j = instruction_number = 0
addx_in_progress = False
while instruction_number < len(instructions):
    instruction = instructions[instruction_number]

    ## CRT Drawing
    if j >= 40:
        print()
        print()
        i += 1
        j = 0
    if i >= 6:
        break
   
    if j in [x, x - 1, x + 1]:
        CRT[i][j] = "#"
    else:
        CRT[i][j] = "."
    print(f"{CRT[i][j]}" , end="")
    j += 1


    ## moving x / sprite
    if instruction == "noop":
        cycles += 1
        instruction_number += 1

    else:
        cycles += 1
        addx_in_progress = (not addx_in_progress)
        if (not addx_in_progress):
            x += int(instruction.split()[1])
            instruction_number += 1

# print(CRT)
with open("op.txt", "w") as f:
    for row in CRT:
        for pixel in row:
            f.write(f"{pixel}")
        f.write("\n")

