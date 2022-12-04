import os
import sys
import re

def puzzle_1():
    good_pairs = 0
    with open(os.path.join(sys.path[0], "puzzle.txt"), "r") as f:
        lines = [re.split('-|,', line[:-1]) for line in f]
    for pairs in lines:
        if int(pairs[0]) >= int(pairs[2]) and int(pairs[1]) <= int(pairs[3]):
            good_pairs += 1
        elif int(pairs[0]) <= int(pairs[2]) and int(pairs[1]) >= int(pairs[3]):
            good_pairs += 1
    return good_pairs

