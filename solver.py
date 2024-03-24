def is_valid(grid, r, c, k):
    in_row = k not in grid[r]
    in_column = k not in [grid[i][c] for i in range(9)]
    in_box = k not in [grid[i][j] for i in range(r//3*3, r//3*3+3) for j in range(c//3*3, c//3*3+3)]
    return in_row and in_column and in_box

def solve_grid(grid, r = 0, c = 0):
    if r == 9:
        return True
    elif c == 9:
        return solve_grid(grid, r + 1, 0)
    elif grid[r][c] != 0:
        return solve_grid(grid, r, c + 1)
    else:
        for k in range (1, 10):
            if is_valid(grid, r, c, k):
                grid[r][c] = k
                if solve_grid(grid, r, c + 1):
                    return True
                grid[r][c] = 0
        return False

def get_grid(file_name):
    f = open(file_name, "r")
    grid = [line.strip() for line in f.readlines()]
    f.close()
    grid = [[int(char) for char in row] for row in grid]
    return grid

i = 0
file_name = input("enter the name file : ")
grid = get_grid(file_name)
solve_grid(grid)
for row in grid:
    if i == 0:
        print("|===================================|")
    print("| ", end="")
    print(*row, sep=" | ", end="")
    print(" |", sep="")
    i += 1
    if (i < 9):
        print("|---+---+---+---+---+---+---+---+---|")
    else:
        print("|===================================|")