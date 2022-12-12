import sys
import os


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
    
    
def puzzle1():
    input = process_input()
    strength = 0
    value = 1
    cycle = 0
    for line in input:
        if cycle % 40 == 19 and cycle < 221:
            if line.startswith("addx"):
                strength += (cycle + 1) * value
        if line.startswith("noop"):
            cycle = noop(cycle)
            if cycle % 40 == 20 and cycle < 221:
                strength += cycle * value
        if line.startswith("addx"):
            added_value = int(line.split()[1])
            cycle, value = addx(cycle, value, added_value)
            if cycle % 40 == 20 and cycle < 221:
                strength += cycle * (value - added_value)
    return strength
