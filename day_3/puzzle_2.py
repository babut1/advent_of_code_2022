import os
import sys


def get_common_item(string_1, string_2, string_3):
    for i in string_1:
        if i in string_2 and i in string_3:
            return i


def get_priority(letter):
    if letter.isupper():
        return ord(letter) - 38
    return ord(letter) - 96


def puzzle_2():
    sum_of_priorities = 0
    with open(os.path.join(sys.path[0], "puzzle.txt"), "r") as f:
        lines = f.readlines()
        lenght = len(lines)
    for i in range(lenght):
        if i % 3 == 0:
            string_1 = lines[i][:-1]
            string_2 = lines[i+1][:-1]
            string_3 = lines[i+2][:-1]
            common_letter = get_common_item(string_1, string_2, string_3)
            sum_of_priorities += get_priority(common_letter)
    return sum_of_priorities
