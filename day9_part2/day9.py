motions = []
with open("ip.txt") as f:
    for line in f:
        direction, steps = line.strip().split()
        motions.append((direction, int(steps)))

head = [0, 0]
tails = []
for _ in range(9):
    tails.append([0, 0])
t_positions = {tuple(tails[len(tails) - 1])}

for direction, steps in motions:

    for step in range(steps):

        # make head move one step 
        if direction == "R":
            head[1] += 1
        elif direction == "U":
            head[0] -= 1
        elif direction == "D":
            head[0] += 1
        else:  # direction == "L"
            head[1] -= 1
        
        i = 0
        last_one_moved = True
        e = False
        while i < len(tails) and last_one_moved:
            if (i + 1 == 3) and (head == [-4, 4]):
                e = True
            last_one_moved = False
            if i == 0:
                h = head
            else:
                h = tails[i - 1]
            t = tails[i]

            t_moved = False

            # head and tail are in same row
            if (h[0] == t[0]):
                if ((h[1] - t[1]) > 1):  # head 2 steps ahead
                    t[1] += 1
                    t_moved = True
                elif ((h[1] - t[1]) < -1):  # head 2 steps behind
                    t[1] -= 1
                    t_moved = True

            # if head and tail are in same column
            elif (h[1] == t[1]):
                if ((h[0] - t[0]) > 1):  # head 2 steps ahead
                    t[0] += 1
                    t_moved = True
                elif ((h[0] - t[0]) < -1):  # head 2 steps behind
                    t[0] -= 1
                    t_moved = True

            # diagonally 2 steps away top right
            elif ((h[0] == t[0] - 1) and (h[1] == t[1] + 2)) or ((h[0] == t[0] - 2) and (h[1] == t[1] + 1)) or ((h[0] <= t[0] - 2) and (h[1] >= t[1] + 2)):
                t[0] -= 1  # up
                t[1] += 1  # right
                t_moved = True
            
            # diagonally 2 steps away top left
            elif ((h[0] == t[0] - 1) and (h[1] == t[1] - 2)) or ((h[0] == t[0] - 2) and (h[1] == t[1] - 1)) or ((h[0] <= t[0] - 2) and (h[1] <= t[1] - 2)):
                t[0] -= 1  # up
                t[1] -= 1  # left
                t_moved = True

            # diagonally 2 steps away bottom right
            elif ((h[0] == t[0] + 1) and (h[1] == t[1] + 2)) or ((h[0] == t[0] + 2) and (h[1] == t[1] + 1)) or ((h[0] >= t[0] + 2) and (h[1] >= t[1] + 2)):
                t[0] += 1  # down
                t[1] += 1  # right
                t_moved = True

            # diagonally 2 steps away bottom left
            elif ((h[0] == t[0] + 1) and (h[1] == t[1] - 2)) or ((h[0] == t[0] + 2) and (h[1] == t[1] - 1)) or ((h[0] >= t[0] + 2) and (h[1] <= t[1] - 2)):
                t[0] += 1  # down
                t[1] -= 1  # right
                t_moved = True

            if t_moved:
                last_one_moved = True
                tails[i] = t
            # print(f"i: {i}, h:{h}, t: {t}, head: {head}") 
            i += 1
            
            t_positions.add(tuple(tails[len(tails) - 1]))
        # print(tails, head)
        # # print()
        # if e:
        #     exit()

print(tails)
print(len(t_positions))



        