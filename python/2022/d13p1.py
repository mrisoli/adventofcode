from utils import obj_list

def compare(v):
    for v1,v2 in zip(*v):
        #print(v1,v2)
        if isinstance(v1, int) and isinstance(v2, int):
            if v1 < v2:
                return False
            elif v1 > v2:
                return True
        if isinstance(v1, int) and not isinstance(v2, int):
            v1 = [v1]
        if not isinstance(v1, int) and isinstance(v2, int):
            v2 = [v2]
        if isinstance(v1, list) and isinstance(v2, list):
            c = compare([v1,v2])
            if c == False:
                return False
            elif c:
                return True
    if len(v[0]) > len(v[1]):
        return True
    return None

l = [[eval(p) for p in v] for v in map(str.split, obj_list(13))]

print(sum([i for i,v in enumerate(l,start=1) if not compare(v)]))
