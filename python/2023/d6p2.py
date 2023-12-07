from utils import str_list
from d6 import ways,parse_num

def parse(l):
    return tuple(map(lambda v: int(''.join(parse_num(v))), l))

print(ways(parse(str_list(6))))
