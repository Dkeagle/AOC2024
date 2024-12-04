def search_word(grid, r, c, dr, dc, index):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    length = len(word)

    if index == length:
        return True

    if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != word[index]:
        return False

    return search_word(grid, r + dr, c + dc, dr, dc, index + 1)

def search_cross(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    
    if r - 1 < 0 or c - 1 < 0 or r + 1 >= rows or c + 1 >= cols: 
        return False

    if grid[r-1][c-1] == "M" and grid[r-1][c+1] == "M" and grid[r+1][c-1] == "S" and grid[r+1][c+1] == "S":
        return True
    elif grid[r-1][c-1] == "M" and grid[r-1][c+1] == "S" and grid[r+1][c-1] == "M" and grid[r+1][c+1] == "S":
        return True
    elif grid[r-1][c-1] == "S" and grid[r-1][c+1] == "M" and grid[r+1][c-1] == "S" and grid[r+1][c+1] == "M":
        return True
    elif grid[r-1][c-1] == "S" and grid[r-1][c+1] == "S" and grid[r+1][c-1] == "M" and grid[r+1][c+1] == "M":
        return True
    else:
        return False
        


def a():
    input = []
    found = 0
    with open("./inputs/day04.txt", "r") as file:
        for line in file: 
            input.append(list(line.strip()))

    directions = [
        (-1, 0),  # Top
        (-1, 1),  # Top Right
        (0, 1),   # Right
        (1, 1),   # Bottom Right
        (1, 0),   # Bottom
        (1, -1),  # Bottom Left
        (0, -1),  # Left
        (-1, -1)  # Top Left
    ]

    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == 'X':
                for dr, dc in directions:
                    if search_word(input, r, c, dr, dc, 0): 
                        found += 1
    return found

def b():
    input = []
    found = 0
    with open("./inputs/day04.txt", "r") as file:
        for line in file:
            input.append(list(line.strip()))

    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "A":
                if search_cross(input, r, c):
                    found += 1
    return found