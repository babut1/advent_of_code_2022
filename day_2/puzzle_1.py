import os
import sys


def puzzle_1():
    with open(os.path.join(sys.path[0], "puzzle.txt"), "r") as f:
        rounds = [(line[0], line[2]) for line in f]
    score = 0
    for round in rounds:
        if round[0] == 'A':
            if round[1] == 'X':
                score += 4
            elif round[1] == 'Y':
                score += 8
            else:
                score += 3
        elif round[0] == 'B':
            if round[1] == 'X':
                score += 1
            elif round[1] == 'Y':
                score += 5
            else:
                score += 9
        else:
            if round[1] == 'X':
                score += 7
            elif round[1] == 'Y':
                score += 2
            else:
                score += 6
    return score
