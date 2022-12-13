packets = []
a = b = None
with open("ip.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            packets.append(eval(line))

packets.append([[2]])
packets.append([[6]])

def compare_lists(l1, l2):
    i = 0
    while (i < len(l1)) and (i < len(l2)):
        a, b = l1[i], l2[i]
        
        # both ints
        if (type(a) == int) and (type(b) == int):
            if a == b:
                i += 1
                continue
            elif a < b:
                return 1
            else:  # a > b
                return -1

        # both lists
        elif (type(a) == list) and (type(b) == list):
            check = compare_lists(a, b)
            if check == 0:
                i += 1
                continue
            else:  # 1 or -1
                return check

        # one list one int
        else:
            if type(a) == int:
                a = [a]
            else:
                b = [b]
            check = compare_lists(a, b)
            if check == 0:
                i += 1
                continue
            else:  # 1 or -1
                return check
    
    if len(l1) < len(l2):
        return 1
    
    elif len(l1) == len(l2):
        return 0

    else:
        return -1

swaps_needed = True
k = 0
while swaps_needed:
    swaps_needed = False

    for i in range(len(packets) - k):
        for j in range(i + 1, len(packets) - k):
            check = compare_lists(packets[i], packets[j])
            if check == -1:
                swaps_needed = True
                packets[i], packets[j] = packets[j], packets[i]
    
    k += 1
        

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))



