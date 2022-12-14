packets_pairs = []
a = b = None
with open("ip.txt") as f:
    for line in f:

        if a == None:
            a = eval(line.strip())
        elif b == None:
            b = eval(line.strip())
        else:
            packets_pairs.append((a, b))
            a = b = None
    
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

ans = 0
for i, (a, b) in enumerate(packets_pairs):
    if compare_lists(a, b) >= 0:
        ans += i + 1

print(ans)
