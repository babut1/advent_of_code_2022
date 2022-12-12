import os
import sys

def process_input():
    input = []
    with open(os.path.join(sys.path[0], "puzzle.txt"), "r") as f:
        for line in f:
            input.append(line[:-1])
    return input


def move(rope, move_direction):
    rope[0][0], rope[0][1] = move_head(rope[0][0], rope[0][1], move_direction)
    for i in range(0, len(rope)-1):
        rope[i+1][0], rope[i+1][1] = move_body(rope[i][0], rope[i][1], rope[i+1][0], rope[i+1][1])
    return rope


def move_body(head_x, head_y, tail_x, tail_y):
    if head_y > tail_y + 1 and head_x > tail_x + 1:
        tail_y += 1
        tail_x += 1
        return tail_x, tail_y
    if head_y > tail_y + 1 and head_x < tail_x - 1:
        tail_y += 1
        tail_x -= 1
        return tail_x, tail_y
    if head_y < tail_y - 1 and head_x < tail_x - 1:
        tail_y -= 1
        tail_x -= 1
        return tail_x, tail_y
    if head_y < tail_y - 1 and head_x > tail_x + 1:
        tail_y -= 1
        tail_x += 1
        return tail_x, tail_y
    if head_y > tail_y + 1:
        tail_y += 1
        tail_x = head_x
    if head_y < tail_y - 1:
        tail_y -= 1
        tail_x = head_x
    if head_x > tail_x + 1:
        tail_x += 1
        tail_y = head_y
    if head_x < tail_x - 1:
        tail_x -= 1
        tail_y = head_y
    return tail_x, tail_y


def move_head(head_x, head_y, move_direction):
    if move_direction == "U":
        head_y += 1
    elif move_direction == "D":
        head_y -= 1
    elif move_direction == "L":
        head_x -= 1
    elif move_direction == "R":
        head_x += 1
    return head_x, head_y


def puzzle_2():
    tail_positions = []
    input = process_input()
    rope = [[0,0] for _ in range(10)]
    for line in input:
        move_amount = int(line.split()[1])
        move_direction = line.split()[0]
        for _ in range(move_amount):
            rope = move(rope, move_direction)
            if [rope[-1][0], rope[-1][1]] not in tail_positions:
                tail_positions.append([rope[-1][0], rope[-1][1]])

    return len(tail_positions)
