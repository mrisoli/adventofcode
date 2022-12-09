from utils import cmd_list

def move_head(c,h):
    d = 1 if c in 'RL' else 0
    v = 1 if c in 'RD' else -1
    h[d] += v
    return h

def move_tail(h,t):
    if abs(h[0] - t[0]) > 0 and abs(h[1] - t[1]) > 0 and abs(h[0] - t[0]) + abs(h[1] - t[1]) > 2:
        t[0] += 1 if h[0] - t[0] > 0 else -1
        t[1] += 1 if h[1] - t[1] > 0 else -1
    elif abs(h[0] - t[0]) > 1:
        t[0] += 1 if h[0] - t[0] > 0 else -1
    elif abs(h[1] - t[1]) > 1:
        t[1] += 1 if h[1] - t[1] > 0 else -1
    return t

def run_cmd(n):
    t = [[0,0] for i in range(n)]
    v = set()
    for c,n in cmd_list(9):
        for i in range(n):
            t[0] = move_head(c,t[0])
            for i in range(1,len(t)):
                t[i] = move_tail(t[i - 1], t[i])
            v.add(tuple(t[-1]))
    print(len(v))
