# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

with open('input/problem11.in') as fin:
    grid = fin.readlines()
    grid = [list(map(int, row.strip().split())) for row in grid]
print(grid)
max_product = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        # vertical
        if row + 3 < len(grid):
            test = grid[row][col] * grid[row + 1][col] * grid[row + 2][col] * grid[row + 3][col]
            if test > max_product:
                max_product = test
        # horizontal
        if col + 3 < len(grid[row]):
            test = grid[row][col] * grid[row][col + 1] * grid[row][col + 2] * grid[row][col + 3]
            if test > max_product:
                max_product = test
        # diagonal 1
        if row + 3 < len(grid) and col + 3 < len(grid[row]):
            test = grid[row][col] * grid[row + 1][col + 1] * grid[row + 2][col + 2] * grid[row + 3][col + 3]
            if test > max_product:
                max_product = test
        # diagonal 2
        if row + 3 < len(grid) and col - 3 >= 0:
            test = grid[row][col] * grid[row + 1][col - 1] * grid[row + 2][col - 2] * grid[row + 3][col - 3]
            if test > max_product:
                max_product = test
        print(row, col)
print(max_product)
