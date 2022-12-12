grid = []
with open("ip.txt") as f:
    for line in f:
        grid.append(list(line.strip()))

print(grid)

# find starting point
start = end = None
for i in range(len(grid)):
    for j in range(len(grid[0])):

        if grid[i][j] == "S":
            start = (i, j)
            grid[i][j] = "a"

        elif grid[i][j] == "E":
            end = (i, j)
            grid[i][j] = "z"

        if start and end:
            break

    if start and end:
        break   

valid_coordinate = lambda x, y: not( (x < 0) or (y < 0) or (x >= len(grid)) or (y >= len(grid[0])) )

queue = [start]
visited = {start}
increments = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]
steps_sofar = 0
while queue:
    
    l = len(queue)
    for _ in range(l):
        x, y = queue.pop(0)
        if (x, y) == end:
            print(steps_sofar)
            exit()
        else:
            for x_increment, y_increment in increments:
                new_x = x + x_increment
                new_y = y + y_increment

                if ((new_x, new_y) in visited) or (not valid_coordinate(new_x, new_y)):
                    continue
                
                # if new square is lower than or equal to, or one step higher than current square
                if ((ord(grid[new_x][new_y])) <= (ord(grid[x][y]))) or ((ord(grid[new_x][new_y])) == (ord(grid[x][y]) + 1)):
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))

    steps_sofar += 1
    print()
print("no result")

