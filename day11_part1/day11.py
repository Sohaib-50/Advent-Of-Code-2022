ROUNDS = 20
monkeys = {}
monkey = 0
with open("ip.txt") as f:
    while True:
        f.readline()  # skipping monkey name line
        items = f.readline().strip().split()[2:]
        for i in range(len(items)):
            items[i] = int(items[i].split(",")[0])
        operation = " ".join(f.readline().strip().split()[3:])
        divisibility_test = int(f.readline().strip().split()[-1])
        if_true = int(f.readline().strip().split()[-1])
        if_false = int(f.readline().strip().split()[-1])

        monkeys[monkey] = {
            "items": items,
            "operation": operation,
            "divisibility_test": divisibility_test,
            "if_true": if_true,
            "if_false": if_false
        }
        monkey += 1

        if not f.readline():
            break
inspections = [0 for _ in range(monkey)]

for rounds in range(ROUNDS):
    for monkey in monkeys:
        for i in range(len(monkeys[monkey]["items"])):
            inspections[monkey] += 1
            item = monkeys[monkey]["items"].pop(0)
            item = eval(monkeys[monkey]["operation"].replace("old", str(item)))
            item = item // 3
            if (item % monkeys[monkey]["divisibility_test"]) == 0:
                monkeys[monkeys[monkey]["if_true"]]["items"].append(item)
            else:
                monkeys[monkeys[monkey]["if_false"]]["items"].append(item)

inspections.sort()
print(inspections[-1] * inspections[-2])