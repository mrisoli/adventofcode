from utils import str_list

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = {}
        self.size = 0

    def add_file(self, size):
        self.size += size
        if self.parent:
            self.parent.add_file(size)

    def add_dir(self, name):
        self.dirs[name] = Dir(name=name, parent=self)

def run_cmd(s, pwd):
    if s.startswith('ls'):
        return pwd
    name = s.split(' ')[1]
    if name == '..':
        return pwd.parent
    elif pwd:
        return pwd.dirs[name]
    else:
        return Dir(name=name, parent=pwd)

def get_tree():
    root, pwd = None,None
    for l in str_list(7):
        if l.startswith('$'):
            pwd = run_cmd(l[2:], pwd)
            if not root:
                root = pwd
        elif l[0].isdigit():
            pwd.add_file(int(l.split(' ')[0]))
        else:
            pwd.add_dir(l.split(' ')[1])
    return root

def navigate(node):
    yield(node)
    for c in node.dirs.values():
        yield from navigate(c)
