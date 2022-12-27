from d19 import calc,parse
from utils import str_list

print(sum(i * calc(b, 24) for i, *b in map(parse, str_list(19))))
