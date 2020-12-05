def find_num(s, l, h):
    if l == h:
        return l
    elif s[0] == 'F':
        return find_num(s[1:], l, (h + l) // 2)
    else:
        return find_num(s[1:], l + ((h - l + 1) // 2), h)

def get_row(s):
    return find_num(s, 0, 127)

def get_col(s):
    return find_num(s.replace('L', 'F'), 0, 7)

def get_seat(s):
    return (8 * get_row(s[0:7])) + get_col(s[7:])
