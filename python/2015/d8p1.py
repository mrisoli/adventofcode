from utils import str_list

def pr(s):
    return len(bytes(s[1:-1], "utf-8").decode("unicode_escape"))

f = str_list(8)
print(sum(map(len, f)) - sum(map(pr, f)))
