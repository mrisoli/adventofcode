from d10 import get_polygon

def det(a, b):
    return a.real * b.imag - a.imag * b.real

def area(p):
    area = abs(sum([det(a,b) for a,b in zip(p, p[1:] +[p[0]])]))
    return  int(((area - len(p))/2) + 1)

print(area(get_polygon()))
