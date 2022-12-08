with open("ip.txt", "r") as f:
    trees_grid = []
    for line in f:
        line = line.strip()
        trees_grid.append([int(i) for i in line])

visible_trees = 0
for row in range(len(trees_grid)):

    # all in 1st and last rows visible
    if (row == 0) or (row == (len(trees_grid) - 1)):
        visible_trees += len(trees_grid[0])
        continue
    

    for col in range(len(trees_grid[0])):

        # 1st and last tree in each row visible
        if (col == 0) or (col == (len(trees_grid[0]) - 1)):
            visible_trees += 1
            continue

        current_tree = trees_grid[row][col]
        any_direction_visible = False

        # move up
        temp_row = row - 1
        current_direction_visible = True
        while (temp_row >= 0) and (not any_direction_visible) and (current_direction_visible):
            if trees_grid[temp_row][col] >= current_tree:
                current_direction_visible = False
            temp_row -= 1
        if current_direction_visible:
            any_direction_visible = True

        # move down
        temp_row = row + 1
        current_direction_visible = True
        while (temp_row < len(trees_grid)) and (not any_direction_visible) and (current_direction_visible):
            if trees_grid[temp_row][col] >= current_tree:
                current_direction_visible = False
            temp_row += 1
        if current_direction_visible:
            any_direction_visible = True
        
        # move right
        temp_col = col + 1
        current_direction_visible = True
        while (temp_col < len(trees_grid[0])) and (not any_direction_visible) and (current_direction_visible):
            if trees_grid[row][temp_col] >= current_tree:
                current_direction_visible = False
            temp_col += 1
        if current_direction_visible:
            any_direction_visible = True

        # move left
        temp_col = col - 1
        current_direction_visible = True
        while (temp_col >= 0) and (not any_direction_visible) and (current_direction_visible):
            if trees_grid[row][temp_col] >= current_tree:
                current_direction_visible = False
            temp_col -= 1
        if current_direction_visible:
            any_direction_visible = True
        
        visible_trees += 1 if any_direction_visible else 0

print(visible_trees)