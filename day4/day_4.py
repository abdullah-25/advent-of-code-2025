def forklift_roll_count(line_of_roles):
    """
    [row][col]
    for every pos, check

    while count of @ != 4:
        l, r = [row][col+1], [row][col-1],
         u, d =  [row+1][col], [row-1][col]
         d1,d2,d3,4 = [row+1][col-1], [row+1][col+1], [row+1][col+1], [row+1][col-1]

    if true: mark it X and add to sum
    if false: continue

    """
    print_roll = '@'
    sum = 0
    neighbor_offsets = [
        (-1, -1), (-1, 0), (-1, 1),  # Top row
        (0, -1),          (0, 1),   # Middle row
        (1, -1),  (1, 0),  (1, 1)    # Bottom row
    ]

    for row in range(len(line_of_roles)):
        for col in range(len(line_of_roles[0])):

            if line_of_roles[row][col] != print_roll:
                continue

            local_count = 0

            for off_row, off_col in neighbor_offsets:
                nr, nc = row + off_row, col + off_col

                if 0 <= nr < len(line_of_roles) and 0 <= nc < len(line_of_roles[0]):
                    neighbour_val = line_of_roles[nr][nc]
                    if neighbour_val == print_roll:
                        local_count += 1
                        # mark it as x

                        # recursively call forklift_roll_count(new_state)

            # after check is complete
            if local_count < 4:
                sum += 1
    return sum


def forklift_roll_count_part_2(grid):
    neighbor_offsets = [
        (-1, -1), (-1, 0), (-1, 1),  # Top row
        (0, -1),          (0, 1),   # Middle row
        (1, -1),  (1, 0),  (1, 1)    # Bottom row
    ]
    print_roll = '@'
    rolls_to_mark = []
    total_removed_count = 0
    # convert each char to list so it can be reasigned with 'X'
    grid = [list(row) for row in grid]

    changed = True
    while changed:
        changed = False
        rolls_to_mark = []

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] != print_roll:
                    continue

                local_count = 0
                for off_row, off_col in neighbor_offsets:
                    nr, nc = row + off_row, col + off_col

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        neighbour_val = grid[nr][nc]
                        if neighbour_val == print_roll:
                            local_count += 1

                if local_count < 4:
                    rolls_to_mark.append((row, col))

        if rolls_to_mark:
            changed = True

            for x, y in rolls_to_mark:
                grid[x][y] = 'X'
                total_removed_count += 1

    return total_removed_count




if __name__ == '__main__':
    with open('test.txt', 'r', encoding='UTF8') as f:
        line_of_rolls = []
        for line in f:
            line_of_rolls.append(line.strip())

        # print(forklift_roll_count(line_of_rolls))
        print(forklift_roll_count_part_2(line_of_rolls))
