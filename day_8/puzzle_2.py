import sys
import os


def process_input():
    input = []
    with open(os.path.join(sys.path[0], "puzzle.txt"), "r") as f:
        for line in f:
            input.append(line[:-1])
    grid = [[] for _ in range(len(input))]
    for num, line in enumerate(input):
        for char in line:
            grid[num].append(int(char))
    return grid


def count_visible_trees_up(grid, x, y):
    visible_trees = 0
    for i in range(x-1, -1, -1):
        if grid[i][y] < grid[x][y]:
            visible_trees += 1
        else:
            break
    return visible_trees


def count_visible_trees_down(grid, x, y):
    visible_trees = 0
    for i in range(x+1, len(grid)):
        if grid[i][y] < grid[x][y]:
            visible_trees += 1
        else:
            break
    return visible_trees


def count_visible_trees_left(grid, x, y):
    visible_trees = 0
    for i in range(y-1, -1, -1):
        if grid[x][i] < grid[x][y]:
            visible_trees += 1
        else:
            break
    return visible_trees


def count_visible_trees_right(grid, x, y):
    visible_trees = 0
    for i in range(y+1, len(grid)):
        if grid[x][i] < grid[x][y]:
            visible_trees += 1
        else:
            visible_trees += 1
            break
    return visible_trees


def puzzle_2():
    max_score = -1
    grid = process_input()
    for x in range(len(grid)):
        for y in range(len(grid)):
            tree_score = count_visible_trees_down(grid, x, y) * count_visible_trees_up(grid, x, y) * count_visible_trees_left(grid, x, y) * count_visible_trees_right(grid, x, y)
            if tree_score > max_score:
                max_score = tree_score
    return max_score
