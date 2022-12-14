import os
import sys

def prepare_data():
    with open(os.path.join(sys.path[0], "puzzle.txt"), "r") as f:
        starting_stacks = []
        moves = []
        for num, line in enumerate(f):
            if num == 0:
                for i in range(len(line)//4):
                    starting_stacks.append([])
            if "move" not in line and "1" not in line:
                for index, char in enumerate(line):
                    if char != " " and char != "[" and char != "]" and char != "\n":
                        starting_stacks[index//4].append(char)
            else:
                moves.append(line.split())
    moves.pop(0)
    for move in moves:
        move.remove('move')
        move.remove('from')
        move.remove('to')
    for stack in starting_stacks:
        stack = stack.reverse()
    return starting_stacks, moves


def move_many(current_stacks, move):
    move_list = []
    for i in range(int(move[0])):
        if len(current_stacks[int(move[1]) - 1]) > 0:
            to_move = current_stacks[int(move[1]) - 1].pop()
            move_list.append(to_move)
    move_list.reverse()
    current_stacks[int(move[2]) - 1] += move_list
    
    
def puzzle_2():
    stacks, moves = prepare_data()
    for move in moves:
        move_many(stacks, move)
    result = ""
    for i in stacks:
        result += i[-1]
    return result
