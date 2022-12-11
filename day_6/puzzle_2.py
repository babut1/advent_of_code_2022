import sys
import os

def puzzle_2():
    with open(os.path.join(sys.path[0], "puzzle.txt"), "r") as f:
        input = ""
        for line in f:
            input += line
    i = 0
    while True:
        try:
            string = input[i:i+14]
            for num, char in enumerate(string):
                if string.count(char) != 1:
                    i += 1
                    break
                if num == 13:
                    return i + 14
        except IndexError:
            return None
