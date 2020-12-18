def pn_eval(r):
    s = []
    for t in r:
        if t in '+*':
            arg1 = s.pop()
            arg2 = s.pop()
            s.append(eval(str(arg1) + t + str(arg2)))
        else:
            s.append(int(t))
    return s.pop()

def get_priority(c):
    if c == '+':
        return 2
    elif c == '*':
        return 1
    else:
        return 0

def infix_to_postfix(i, priority):
    e = '(' + i + ')'
    o = ""
    s = []
    for c in e:
        if c.isdigit():
            o += c
        elif c == '(':
            s.append(c)
        elif c == ')':
            while s[-1] != '(':
                o += s.pop()
            s.pop()
        else:
            if priority:
                while get_priority(c) <= get_priority(s[-1]):
                    o += s.pop()
            s.append(c)
    return o

def solve(s, priority):
    t = 0
    e = s.replace(' ', '').replace('(','p').replace(')', '(').replace('p',')')[::-1]
    r = infix_to_postfix(e, priority)
    return pn_eval(r)
