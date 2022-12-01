import os
import sys

def puzzle_2():
    with open(os.path.join(sys.path[0], "puzzle.txt"), "r") as f:
        max_list = [0, 0, 0]
        current_sum = 0
        for line in f:
            if line == "\n":
                if current_sum > max_list[0]:
                    max_list[0] = current_sum
                    max_list = sorted(max_list)
                current_sum = 0
            else:
                current_sum += int(line)
        return sum(max_list)
