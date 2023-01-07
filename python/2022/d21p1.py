from utils import str_list

f = [x.replace(':', '=') for x in str_list(21)]
root = None
while not root:
    for p in f:
        try:
            exec(p)
        except NameError:
            continue
print(int(root))
