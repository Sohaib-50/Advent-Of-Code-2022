instructions = []
with open("ip.txt") as f:
    for line in f:
        instructions.append(line.strip())

cycles = 1
x = 1
required_cycles = {20, 60, 100, 140, 180, 220}
ans = 0
for instruction in instructions:
    if instruction == "noop":
        cycles += 1
        if cycles in required_cycles:
            ans += (x * cycles)

    else:
        cycles += 1
        if cycles in required_cycles:
            ans += (x * cycles)

        cycles += 1
        x += int(instruction.split()[1])
        if cycles in required_cycles:
            ans += (x * cycles)

print(ans)


