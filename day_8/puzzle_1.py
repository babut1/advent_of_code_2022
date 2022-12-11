import sys
import os


def process_input():
    input = []
    with open(os.path.join(sys.path[0], "puzzle.txt"), "r") as f:
        for line in f:
            input.append(line[:-1])
    grid = [[] for i in range(len(input))]
    for num, line in enumerate(input):
        for char in line:
            grid[num].append(int(char))
    return grid


def check_if_visible(grid, x, y):
    if x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid) - 1:
        return True
    return check_if_visible_horizontally(grid, x, y) or check_if_visible_vertically(grid, x, y)
    

def check_if_visible_left_horizontally(grid, x, y):
    for i in range(y):
        if grid[x][i] >= grid[x][y]:
            return False
    return True


def check_if_visible_right_horizontally(grid, x, y):
    for i in range(y + 1, len(grid)):
        if grid[x][i] >= grid[x][y]:
            return False
    return True


def check_if_visible_horizontally(grid, x, y):
    return check_if_visible_left_horizontally(grid, x, y) or check_if_visible_right_horizontally(grid, x, y)


def check_if_visible_top_vertially(grid, x, y):
    for i in range(x):
        if grid[i][y] >= grid[x][y]:
            return False
    return True


def check_if_visible_down_vertially(grid, x, y):
    for i in range(x + 1, len(grid)):
        if grid[i][y] >= grid[x][y]:
            return False
    return True


def check_if_visible_vertically(grid, x, y):
    return check_if_visible_top_vertially(grid, x, y) or check_if_visible_down_vertially(grid, x, y)


def puzzle_1():
    visible_trees = 0
    grid = process_input()
    for x in range(len(grid)):
        for y in range(len(grid)):
            print(x, y, check_if_visible(grid, x, y), grid[x][y])
            if check_if_visible(grid, x, y):
                visible_trees += 1
    return visible_trees
