motions = []
with open("ip.txt") as f:
    for line in f:
        direction, steps = line.strip().split()
        motions.append((direction, int(steps)))

h = [0, 0]
t = [0, 0]
t_positions = {tuple(t)}

for direction, steps in motions:

    for step in range(steps):
        print(h, t)
        t_moved = False

        # make head move one step 
        if direction == "R":
            h[1] += 1
        elif direction == "U":
            h[0] -= 1
        elif direction == "D":
            h[0] += 1
        else:  # direction == "L"
            h[1] -= 1

        # head and tail are in same row
        if (h[0] == t[0]):
            if ((h[1] - t[1]) == 2):  # head 2 steps ahead
                t[1] += 1
                t_moved = True
            elif ((h[1] - t[1]) == -2):  # head 2 steps behind
                t[1] -= 1
                t_moved = True

        # if head and tail are in same column
        elif (h[1] == t[1]):
            if ((h[0] - t[0]) == 2):  # head 2 steps ahead
                t[0] += 1
                t_moved = True
            elif ((h[0] - t[0]) == -2):  # head 2 steps behind
                t[0] -= 1
                t_moved = True

        # diagonally 2 steps away top right
        elif ((h[0] == t[0] - 1) and (h[1] == t[1] + 2)) or ((h[0] == t[0] - 2) and (h[1] == t[1] + 1)):
            t[0] -= 1  # up
            t[1] += 1  # right
            t_moved = True
        
        # diagonally 2 steps away top left
        elif ((h[0] == t[0] - 1) and (h[1] == t[1] - 2)) or ((h[0] == t[0] - 2) and (h[1] == t[1] - 1)):
            t[0] -= 1  # up
            t[1] -= 1  # left
            t_moved = True

        # diagonally 2 steps away bottom right
        elif ((h[0] == t[0] + 1) and (h[1] == t[1] + 2)) or ((h[0] == t[0] + 2) and (h[1] == t[1] + 1)):
            t[0] += 1  # down
            t[1] += 1  # right
            t_moved = True

        # diagonally 2 steps away bottom left
        elif ((h[0] == t[0] + 1) and (h[1] == t[1] - 2)) or ((h[0] == t[0] + 2) and (h[1] == t[1] - 1)):
            t[0] += 1  # down
            t[1] -= 1  # right
            t_moved = True

        t_positions.add(tuple(t))
    print()
print(len(t_positions))



        