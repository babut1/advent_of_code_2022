import os
import sys


def process_input():
    input = []
    with open(os.path.join(sys.path[0], "puzzle.txt"), "r") as f:
        for line in f:
            input.append(line[:-1])
    return input
    
    
def noop(cycle):
    return cycle + 1


def addx(cycle, value, added_value):
    cycle += 2
    value += added_value
    return cycle, value


def puzzle_2():
    input = process_input()
    value = 1
    cycle = 0
    circuits = ["#" for _ in range(241)]
    sprite_indxes = [0, 1, 2]
    for line in input:
        if line.startswith("noop"):
            cycle = noop(cycle)
            if cycle % 40 not in sprite_indxes:
                circuits[cycle] = "."
        if line.startswith("addx"):
            added_value = int(line.split()[1])
            cycle, value = addx(cycle, value, added_value)
            sprite_indxes = [value - 1, value, value + 1]
            if cycle % 40 not in sprite_indxes:
                circuits[cycle] = "."
            if (cycle - 1) % 40 not in [value - 1 - added_value, value - added_value, value + 1 - added_value]:
                circuits[cycle - 1] = "."
    print_solution(circuits)
    return circuits
    
    
def print_solution(circuits):
    result = ""
    for i in range(0, 240):
        if i % 40 == 0 and i:
            result += "\n"
        result += circuits[i]
    print(result)
