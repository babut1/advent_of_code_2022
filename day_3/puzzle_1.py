import os
import sys


def get_common_item(string_1, string_2):
    for i in string_1:
        if i in string_2:
            return i


def get_priority(letter):
    if letter.isupper():
        return ord(letter) - 38
    return ord(letter) - 96


def puzzle_1():
    sum_of_priorities = 0
    with open(os.path.join(sys.path[0], "puzzle.txt"), "r") as f:
        for line in f:
            line = line[:-1]
            string_1, string_2 = line[:len(line)//2], line[len(line)//2:]
            common_letter = get_common_item(string_1, string_2)
            sum_of_priorities += get_priority(common_letter)
    return sum_of_priorities
