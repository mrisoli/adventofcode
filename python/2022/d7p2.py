from d7 import get_tree,navigate

node = get_tree()
needed_size = 70000000 - node.size
print(min([v.size for v in navigate(node) if needed_size + v.size >= 30000000]))
