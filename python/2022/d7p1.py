from d7 import get_tree,navigate

print(sum([v.size for v in navigate(get_tree()) if v.size <= 100000]))
