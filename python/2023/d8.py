from utils import str_list

class Node:
    def __init__(self, data):
        name, dirs = map(str.strip, data.split('='))
        left,right = map(str.strip, dirs[1:-1].split(','))
        self.name = name
        self.left = left
        self.right = right

def init():
    d,_, *m = str_list(8)
    return d,{x.name:x for x in map(Node, m)}
