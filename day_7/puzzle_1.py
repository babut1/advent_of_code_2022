import os
import sys


class tree:
    def __init__(self, root):
        self.root = root
        self.current_dir = root
        self.sum_of_sizes_under_100000 = 0
    
    def set_current_dir(self, dir):
        self.current_dir = dir

    def get_current_dir(self):
        return self.current_dir

    def count_sum_of_sizes_under_100000(self, current_dir):
        if current_dir.size < 100000:
            self.sum_of_sizes_under_100000 += current_dir.size
        for kid in current_dir.kids:
            current_dir = kid
            self.count_sum_of_sizes_under_100000(current_dir)
        return self.sum_of_sizes_under_100000


class directory:
    def __init__(self, parent, name):
        self.parent = parent
        self.size = 0
        self.name = name
        self.kids = []

    def add_size(self, size):
        self.size += size
    
    def get_parent(self):
        return self.parent

    def add_kids(self, kid):
        self.kids.append(kid)

    def get_size(self):
        return self.size


def get_input():
    input = []
    with open(os.path.join(sys.path[0], "puzzle.txt"), "r") as f:
        for line in f:
            input.append(line[:-1])
    return input


def process_input():
    input = get_input()
    dir_tree = tree(directory(None, input[0]))
    input.pop(0)
    for i in input:
        if i.startswith("$ cd"):
            if i.startswith("$ cd .."):
                dir_tree.set_current_dir(dir_tree.current_dir.parent)
            else:
                new_dir = directory(dir_tree.current_dir, i.split()[-1])
                curr_dir = dir_tree.get_current_dir()
                curr_dir.add_kids(new_dir)
                dir_tree.set_current_dir(new_dir)
        elif i.startswith("$ ls") or i.startswith("dir"):
            continue
        else:
            curr_dir = dir_tree.get_current_dir()
            parent = curr_dir.parent
            curr_dir.add_size(int(i.split()[0]))
            while parent is not None:
                curr_dir = curr_dir.parent
                parent = parent.parent
                curr_dir.add_size(int(i.split()[0]))
    return dir_tree


def puzzle_1():
    dir_tree = process_input()
    result = dir_tree.count_sum_of_sizes_under_100000(dir_tree.root)
    return result
