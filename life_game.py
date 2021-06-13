import random
import copy
import time
# https://robertheaton.com/2018/07/20/project-2-game-of-life/

def generate_grid(n):
    grid = [[random.choice((0, 1)) for x in range(n)] for y in range(n)]

    return grid


def render(grid):
    print_ready = []
    for y in grid:
        col = []
        for x in y:
            if x == 1:
                col.append('#')
            else:
                col.append(' ')
        print_ready.append(col)

    # print_ready = [[random.choice(CHARACTERS) for x in y] for y in grid]
    for column in print_ready:
        print(column)
    print()


def neighbors(grid, rowNumber, columnNumber, radius=1):
    rowNumber += 1
    columnNumber += 1
    new_grid = [[grid[i][j] if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) else 0
                for j in range(columnNumber-1-radius, columnNumber+radius)]
                for i in range(rowNumber-1-radius, rowNumber+radius)]
    new_grid[1][1] = 0

    return sum(sum(new_grid, []))


def change_value(grid):
    new_grid = copy.deepcopy(grid)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            count = neighbors(grid, i, j)
            if count < 2:
                new_grid[i][j] = 0
            if (count == 2 or count == 3) and grid[i][j] == 1:
                pass
            if count > 3:
                new_grid[i][j] = 0
            if count == 3 and grid[i][j] == 0:
                new_grid[i][j] = 1

    return new_grid


n = 100
grid = generate_grid(n)

while True:
    grid = change_value(grid)
    render(grid)
