from d13 import make, cmp

print(sum(i for i,v in enumerate(make(),1) if cmp(*v) <= 0))
