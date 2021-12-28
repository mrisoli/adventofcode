from collections import deque
from utils import fopen

hallway = [0,1,3,5,7,9,10]
rooms = [2,4,6,8]
final = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
en = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

class HallwayPos:
    def __init__(self, state, n, l):
        self.s = state
        self.pos = n
        self.label = l

    def get_move(self):
        rn = final[self.label]
        room = self.s.state[rn]
        d = None
        st = 1 if self.pos > rn else -1
        mv = not any([self.s.state[i] for i in range(rn, self.pos, st) if i in hallway])
        if not mv:
            return None
        for r in range(len(room) - 1, 0, -1):
            if room[r] and room[r] != self.label:
                return None
            if not d and not room[r]:
                d = r
                break
        return self.move(rn, d)

    def move(self, room, d):
        v = [x[:] if i in rooms else x for i,x in enumerate(self.s.state)]
        v[self.pos] = None
        v[room][d] = self.label
        return State(v, self.s.e + (en[self.label] * (d + abs(room - self.pos))))

class RoomPos:
    def __init__(self, state, l, d, n):
        self.s = state
        self.label = l
        self.depth = d
        self.pos = n

    def move(self, h):
        st = 1 if h > self.pos else -1
        move = not any([self.s.state[i] for i in range(self.pos, h, st) if i in hallway])
        if not move:
            return None
        v = [x[:] if i in rooms else x for i,x in enumerate(self.s.state)]
        v[self.pos][self.depth] = None
        v[h] = self.label
        return State(v, self.s.e + (en[self.label] * (self.depth + abs(h - self.pos))))

    def get_moves(self):
        t = []
        for h in hallway:
            if not self.s.state[h]:
                s = self.move(h)
                if s: t.append(s)
        return t

    def not_final(self):
        room = self.s.state[self.pos]
        return self.pos != final[self.label] or any(map(lambda x: x is not None and x != self.label, room))

class Solution:
    def __init__(self, s):
        self.s = len(s[rooms[0]]) - 1

    def check(self, candidate):
        return all([([k] * self.s) == candidate.state[v][1:] for k,v in final.items()])

class State:
    def __init__(self, s, e):
        self.state = s
        self.e = e

    def move(self, s, f, d=0):
        v = [x[:] if i in rooms else x for i,x in enumerate(self.state)]
        st = 1 if f > s else -1
        for p in range(s, f, st):
            if p not in rooms and self.state[p]:
                return None
        if d > 0:
            e = v[s][d]
            v[s][d] = None
            v[f] = e
            return (v, d + abs(f - s))
        else:
            t = 1 + next((i for i,x in enumerate(self.state[s][1:]) if not x), None)
            e = v[s]
            v[s] = None
            v[f][t] = e
            return (v, t + abs(f - s))
        return None

    def get_hallway(self):
        c = [HallwayPos(self, i, self.state[i]) for i in hallway if self.state[i]]
        c = [x.get_move() for x in c]
        return [x for x in c if x]

    def get_room(self):
        c = []
        for i in rooms:
            x = self.state[i]
            t = next(((ii, xx) for ii,xx in enumerate(x) if xx), None)
            if t:
                n,t = t
                rp = RoomPos(self, t, n, i)
                if rp.not_final(): c.append(rp)
        s = []
        for ca in c:
            s += ca.get_moves()
        return [x for x in s if x]

    def get_candidates(self):
        c = self.get_hallway() + self.get_room()
        return sorted(c, key=lambda x: x.e)

def setup(fold):
    extra = [['D','D'],['C','B'],['B','A'],['A','C']]
    f = list(zip(*map(lambda x: x.strip().replace('#', ''), fopen(23).readlines()[2:4])))
    h = [None] * 11
    for i in range(len(h)):
        if i in rooms and f:
            e = []
            if fold:
                e = extra[0]
                extra = extra[1:]
            h[i] = [h[i]] + [f[0][0]] + e + [f[0][1]]
            f = f[1:]
    return h


def run(state, solution):
    states = deque()
    states.append(state)
    s = 999999999
    v = {}
    while states:
        candidate = states.pop()
        v[str(candidate.state)] = candidate.e
        if solution.check(candidate):
            if candidate.e < s:
                s = candidate.e
        else:
            new_cs = candidate.get_candidates()
            new_cs.reverse()
            for cs in new_cs:
                ss = str(cs.state)
                if ss in v and cs.e >= v[ss]:
                    continue
                states.append(cs)
    return s

def solve(fold=False):
    h = setup(fold)
    solution = Solution(h)
    initial = State(h, 0)
    print(run(initial, solution))
