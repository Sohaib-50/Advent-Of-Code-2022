# import the rocks list from day17_part1\rocks.py
from rocks import rocks_list as rocks

with open("ip.txt") as f:
    directions = f.read().strip()

chamber = [["." for _ in range(7)]]

print("Initial chamber:")
for row in chamber:
    print("".join(row))

last_row = 1
rock_cells_in_last_row = []
rock_index = direction_index = 0
CHAMBER_WIDTH = 7
LIMIT = 2022
while rock_index < LIMIT:
    rock = rocks[rock_index % len(rocks)]
    rock = rock.split("\n")
    rock = [list(row) for row in rock]

    # # make the rock list like it is inside the chamber, i.e. 7 cells wide. The right edge should be 2 cells away from the left edge
    # for row in rock:
    #     for _ in range(2):
    #         row.insert(0, ".")
    # for row in rock:
    #     print("".join(row))

    rock_top = 0
    rock_bottom = len(rock) - 1
    rock_left = 2

    for _ in range(len(rock) + 2):
        # chamber.append(["." for _ in range(CHAMBER_WIDTH)])
        chamber.insert(0, ["." for _ in range(CHAMBER_WIDTH)])

    # print("Chamber after adding rows:")
    # for row in chamber:
    #     print("".join(row))

    # # simulate adding the rock to top of the chamber
    # chamber_copy = [row[:] for row in chamber]
    # for row in range(rock_top, rock_bottom + 1):
    #     for col in range(rock_left, rock_left + len(rock[0])):
    #         chamber_copy[row][col] = rock[row - rock_top][col - rock_left]

    at_rest = False
    while not at_rest:

        # push the rock according to the direction
        direction = directions[direction_index % len(directions)]
        rock_right = rock_left + len(rock[0]) - 1
        if direction == ">" and ((rock_right + 1) < CHAMBER_WIDTH):
            rock_left += 1
        elif direction == "<" and ((rock_left - 1) >= 0):
            rock_left -= 1
        direction_index += 1

        # check if it is colliding with any other rock, then stop the simulation
        for row in range(rock_top, rock_bottom + 1):
            if at_rest:
                break
            for col in range(rock_left, rock_left + len(rock[0])):
                if chamber[row][col] == "#":

                    # reverse the last move
                    if direction == ">":
                        rock_left -= 1
                    elif direction == "<":
                        rock_left += 1

                    at_rest = True
                    break

        # move rock down
        rock_top += 1
        rock_bottom += 1
        if rock_bottom >= len(chamber):
            # reverse the last move
            rock_top -= 1
            rock_bottom -= 1
            at_rest = True
            break

        # check if it is colliding with any other rock or out of bounds, then stop the simulation
        for row in range(rock_top, rock_bottom + 1):
            if at_rest:
                break
            # if row >= len(chamber):
            #     # reverse the last move
            #     rock_top -= 1
            #     rock_bottom -= 1
            #     at_rest = True
            #     break
            for col in range(rock_left, rock_left + len(rock[0])):
                if chamber[row][col] == "#":

                    # reverse the last move
                    rock_top -= 1
                    rock_bottom -= 1

                    at_rest = True
                    break

    # push the rock according to the direction
    direction = directions[direction_index % len(directions)]
    rock_right = rock_left + len(rock[0]) - 1
    if direction == ">" and ((rock_right + 1) < CHAMBER_WIDTH):
        rock_left += 1
    elif direction == "<" and ((rock_left - 1) >= 0):
        rock_left -= 1
    direction_index += 1

    # check if it is colliding with any other rock, then stop the simulation
    for row in range(rock_top, rock_bottom + 1):
        if at_rest:
            break
        for col in range(rock_left, rock_left + len(rock[0])):
            if chamber[row][col] == "#":

                # reverse the last move
                if direction == ">":
                    rock_left -= 1
                elif direction == "<":
                    rock_left += 1

                at_rest = True
                break


    # place the rock in the chamber
    for row in range(rock_top, rock_bottom + 1):
        for col in range(rock_left, rock_left + len(rock[0])):
            # print(len(chamber), row)
            chamber[row][col] = rock[row - rock_top][col - rock_left]

    # print("Chamber after adding rock:")
    # for row in chamber:
    #     print("".join(row))

    rock_index += 1
    # if rock_index == 2:
    #     exit()
    print(rock_index)

# print height of tower of rocks
i = 0
for row in chamber[::-1]:
    if not ("#" in row):
        print("Height of tower of rocks:", i)
        break
    i += 1
