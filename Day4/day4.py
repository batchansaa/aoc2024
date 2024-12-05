grid = []
with open("Day4/puzzle.txt") as f:
    for line in f:
        grid.append(line.strip())

def count_occurences():
    target = 'XMAS'
    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (0, 1),  # Right
        (0, -1), # Left
        (1, 0),  # Down
        (-1, 0), # Up
        (1, 1),  # Diagonal down-right
        (-1, -1),# Diagonal up-left
        (1, -1), # Diagonal down-left
        (-1, 1)  # Diagonal up-right
    ]

    def check_direction(r, c, dr, dc):
        for i in range(4):
            nr, nc = r + i*dr, c +i*dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != target[i]:
                return False
        return True
    
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == target[0]:
                for dr, dc in directions:
                    if check_direction(r, c, dr, dc):
                        count += 1

    print(count)

def count_x_mas_patterns():
    rows = len(grid)
    cols = len(grid[0])
    target = "MAS"
    reverse_target = target[::-1]

    def check_x_mas(r, c):
        if (r - 1 >= 0 and r + 1 < rows and
            c - 1 >= 0 and c + 1 < cols):

            tl_br = grid[r - 1][c - 1] + grid[r][c] + grid[r + 1][c + 1]

            tr_bl = grid[r - 1][c + 1] + grid[r][c] + grid[r + 1][c - 1]

            return((tl_br in (target, reverse_target)) and 
                   (tr_bl in (target, reverse_target)))

        return False

    count = 0
    for r in range(rows):
        for c in range(cols):
            if check_x_mas(r, c):
                count += 1

    print(count)

count_x_mas_patterns() 

