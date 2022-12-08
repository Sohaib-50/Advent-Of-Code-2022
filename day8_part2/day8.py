with open("ip.txt", "r") as f:
    trees_grid = []
    for line in f:
        line = line.strip()
        trees_grid.append([int(i) for i in line])


max_scenic_score = 0
for row in range(len(trees_grid)):
    

    for col in range(len(trees_grid[0])):
        current_tree = trees_grid[row][col]
        current_scenic_score = 1

        # move up
        temp_row = row - 1
        current_direction_score = 0
        while (temp_row >= 0):
            current_direction_score += 1
            if (trees_grid[temp_row][col] >= current_tree):
                break
            temp_row -= 1
        # print(current_direction_score, end =", ")
        # print(current_scenic_score, current_direction_score)
        current_scenic_score *= current_direction_score

        # move down
        temp_row = row + 1
        current_direction_score = 0
        while (temp_row < len(trees_grid)):
            current_direction_score += 1
            if (trees_grid[temp_row][col] >= current_tree):
                break
            temp_row += 1
        # print(current_direction_score, end =", ")
        current_scenic_score *= current_direction_score
        
        # move right
        temp_col = col + 1
        current_direction_score = 0
        while (temp_col < len(trees_grid[0])):
            current_direction_score += 1
            if (trees_grid[row][temp_col] >= current_tree):
                break
            temp_col += 1
        print(current_direction_score, end =", ")
        current_scenic_score *= current_direction_score

        # move left
        temp_col = col - 1
        current_direction_score = 0
        while (temp_col >= 0):
            current_direction_score += 1
            if (trees_grid[row][temp_col] >= current_tree):
                break
            temp_col -= 1
        # print(current_direction_score, end=" - ")
        current_scenic_score *= current_direction_score

        # print(f"{current_scenic_score} ({row}, {col})")
        
        max_scenic_score = max(current_scenic_score, max_scenic_score)

print(max_scenic_score)