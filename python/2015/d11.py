from utils import str_list

mx = ord('z')
mn = ord('a')

# check if a list of numbers has three consecutive number's
def has_three_seq(s):
    for i in range(len(s) - 2):
        if s[i] + 1 == s[i+1] and s[i+1] + 1 == s[i+2]:
            return True
    return False

# check if a list of numbers has i, o, or l
def has_iol(s):
    for c in s:
        if c == ord('i') or c == ord('o') or c == ord('l'):
            return True
    return False

# check if a list of numbers has two pairs of letter's
def has_two_pairs(s):
    pairs = 0
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            pairs += 1
            i += 2
        else:
            i += 1
    return pairs >= 2

def check(s):
    return has_three_seq(s) and not has_iol(s) and has_two_pairs(s)


# increment a list of numbers and loop around when going over the max
def increment(s):
    i = len(s) - 1
    while i >= 0:
        s[i] += 1
        if s[i] > mx:
            s[i] = mn
            i -= 1
        else:
            break
    return s

def get_seed():
    return list(map(ord, str_list(11)[0]))
