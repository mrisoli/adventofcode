from utils import str_list

VALS = ['A','B','C']
V = {'A': 1, 'B': 2, 'C': 3}
RES = {'W': 6, 'D': 3, 'L': 0}

def play(v,r):
    return RES[r] + V[v]
