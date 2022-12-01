import os
import sys

def puzzle_1():
    with open(os.path.join(sys.path[0], "puzzle.txt"), "r") as f:
        max = 0
        current_sum = 0
        for line in f:
            if line == "\n":
                if current_sum > max:
                    max = current_sum
                current_sum = 0
            else:
                current_sum += int(line)
        return max
