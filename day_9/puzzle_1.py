import os
import sys

def process_input():
    input = []
    with open(os.path.join(sys.path[0], "puzzle.txt"), "r") as f:
        for line in f:
            input.append(line[:-1])
    return input


def move(head_x, head_y, tail_x, tail_y, move_direction):
    if move_direction == "U":
        if head_y > tail_y:
            head_y += 1
            tail_y += 1
            tail_x = head_x
        else:
            head_y += 1
    elif move_direction == "D":
        if head_y < tail_y:
            head_y -= 1
            tail_y -= 1
            tail_x = head_x
        else:
             head_y -= 1
    elif move_direction == "R":
        if head_x > tail_x:
            head_x += 1
            tail_x += 1
            tail_y = head_y
        else:
             head_x += 1
    elif move_direction == "L":
        if head_x < tail_x:
            head_x -= 1
            tail_x -= 1
            tail_y = head_y
        else:
            head_x -= 1
    return head_x, head_y, tail_x, tail_y


def puzzle_1():
    tail_positions = []
    input = process_input()
    head_x = 0
    head_y = 0
    tail_x = 0
    tail_y = 0
    tail_positions.append((tail_x, tail_y))
    for line in input:
        move_amount = int(line.split()[1])
        move_direction = line.split()[0]
        for i in range(move_amount):
            head_x, head_y, tail_x, tail_y = move(head_x, head_y, tail_x, tail_y, move_direction)
            if (tail_x, tail_y) not in tail_positions:
                tail_positions.append((tail_x, tail_y))
    return len(tail_positions)

print(puzzle_1())