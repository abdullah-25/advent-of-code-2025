# def teleportation(rows):
#     row = len(rows)
#     col = len(rows[0])

#     split_count = 0
#     char_as_list = []

#     for r in range(row):
#         for c in range(col):
#             chars = list(rows[r][c])
#             char_as_list.append(chars)
    
#     for line in char_as_list:
#         print(line, end = '\n')
        
#     counted_splits = set()

#     for r in range(len(char_as_list)):
#         for c in range(len(char_as_list[0])):
#             if char_as_list[r][c] == 'S':
#                 r = r + 1
#                 char_as_list[r][c] = '|'
#                 break
#             if char_as_list[r][c] == '^' and (r, c) not in counted_splits:
#                 c_left = c - 1
#                 char_as_list[r][c_left] = '|'
#                 c_right = c + 1
#                 char_as_list[r][c_right] = '|'
#                 split_count += 1
#                 counted_splits.add((r, c))
#             if r > 0 and char_as_list[r][c] == '.' and char_as_list[r-1][c] == '|':
#                 char_as_list[r][c] = '|'
                

#     for line in char_as_list:
#         print(line, end = '\n')
        
#     print(split_count)
    
#     return split_count

from collections import deque

def teleportation(grid):
    R = len(grid)
    C = len(grid[0])

    g = [list(row) for row in grid]

    # find S
    start_c = None
    for c in range(C):
        if grid[0][c] == 'S':
            start_c = c
            break
    
    # Queue for active beams
    q = deque()
    q.append((1, start_c))
    
    visited = set()
    split_count = 0

    while q:
        r, c = q.popleft()

        if r < 0 or r >= R or c < 0 or c >=C:
            continue

        if (r,c) in visited:
            continue
        visited.add((r,c))

        cell = grid[r][c]
        print(cell)
        
        if cell == '.':
            grid[r][c] = '|'
            q.append((r+1, c)) # continue downward

        elif cell == '|':
            q.append((r+1, c))
        
        elif cell == '^':
            split_count += 1
            print(split_count)
            # spaw beams left and right
            q.append((r, c-1))
            q.append((r, c+1))

    return split_count

if __name__ == '__main__':
    with open('test.txt', 'r', encoding='UTF8') as f:
        rows = []
        for line in f:
            rows.append(list(line.rstrip('\n')))
    for row in rows:
        print(repr(row))

    print(teleportation(rows))