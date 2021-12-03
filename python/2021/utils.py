import sys

def get_path(n):
    t = 't' if len(sys.argv) > 1 else 'i'
    return 'inputs/' + t + str(n) + '.in'

def int_list(n):
    return [*map(int, open(get_path(n)))]

def get_cmd(s):
    (c, d) = s.split(' ')
    return (c, int(d))

def cmd_list(n):
    return [*map(get_cmd, open(get_path(n)))]

def str_list(n):
    return [*map(str.strip, open(get_path(n)))]
