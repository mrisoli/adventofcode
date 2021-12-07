import sys

def get_path(n):
    t = 't' if len(sys.argv) > 1 else 'i'
    return 'inputs/' + t + str(n) + '.in'

def int_list(n):
    return [*map(int, fopen(n))]

def int_row(n):
    return [*map(int, fopen(n).readline().split(','))]

def get_cmd(s):
    (c, d) = s.split(' ')
    return (c, int(d))

def cmd_list(n):
    return [*map(get_cmd, fopen(n))]

def str_list(n):
    return [*map(str.strip, fopen(n))]

def fopen(n):
    return open(get_path(n))
