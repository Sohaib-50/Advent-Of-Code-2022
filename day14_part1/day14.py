lines = []
with open("ip.txt") as f:
    for line in f:
        line = line.strip()
        line = line.split(" -> ")
        line = [eval(i) for i in line]
        lines.append(line)


y_min = float('inf')
y_max = float('-inf')
x_min = float('inf')
x_max = float('-inf')
for line in lines:
    for i in range(len(line)):
        coordinate = line[i]
        line[i] = (coordinate[1], coordinate[0])
        coordinate = line[i]
        y_max = max(y_max, coordinate[1])
        y_min = min(y_min, coordinate[1])
        x_max = max(x_max, coordinate[0])
        x_min = min(x_min, coordinate[0])
for line in lines:
    for i in range(len(line)):
        coordinate = line[i]
        line[i] = (coordinate[0], coordinate[1] - y_min)
grid = [["." for i in range(y_min, y_max + 1)] for j in range(0, x_max + 1)]  # initialized as all air

valid_coordinate = lambda x, y: ((x >= 0) and (y >= 0) and (x < len(grid)) and (y < len(grid[0])))

# draw rocks 
for line in lines:
    for i in range(1, len(line)):
        current = line[i]
        prev = line[i - 1]
        if prev[0] == current[0]:
            x = prev[0]
            y_start = min(prev[1], current[1])
            y_end = max(prev[1], current[1])
            for y in range(y_start, y_end + 1):
                grid[x][y] = "#"
        else:
            y = prev[1] 
            x_start = min(prev[0], current[0])
            x_end = max(prev[0], current[0])
            for x in range(x_start, x_end + 1):
                grid[x][y] = "#"

grid[0][500 - y_min] = "+"  # mark source of sand


sand_units = 0
stop = False    
while not stop:
    sand = (0, 500 - y_min)
    x_inc, y_inc = 1, 0  # try moving down first
     
    at_rest = False
    while not at_rest:
        new_x, new_y = (sand[0] + x_inc, sand[1] + y_inc)

        if not valid_coordinate(new_x, new_y):
            at_rest = True
            stop = True
            continue

        # clear, can move    
        if (grid[new_x][new_y] != "#") and (grid[new_x][new_y] != "O"):
            sand = (new_x, new_y)  # update sand
            y_inc = 0  # reset to down movement
        
        # if hit a sand or rock and currently moving down, start trying moving down-left
        elif ((grid[new_x][new_y] == "#") or (grid[new_x][new_y] == "O")) and (y_inc == 0):
            y_inc = -1  # to move left
        
        # if hit a sand or rock and currently moving down-left, start trying moving down-right
        elif ((grid[new_x][new_y] == "#") or (grid[new_x][new_y] == "O")) and (y_inc == -1):
            y_inc = 1  # to move left

        # if hit a sand or rock and currently moving down-right, stop and store sand
        elif ((grid[new_x][new_y] == "#") or (grid[new_x][new_y] == "O")) and (y_inc == 1):
            grid[sand[0]][sand[1]] = "O"
            at_rest = True
        
    sand_units += 1

            
with open("op.txt", "w") as f:
    for row in grid:
        f.write(f"{''.join(row)}\n")

print(sand_units - 1)





    
    
