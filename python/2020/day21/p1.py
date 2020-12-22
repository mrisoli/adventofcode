from common import allergens
f = open('p.in').read().splitlines()
(s, a) = allergens.get_data(f)
for v in s.values():
    for i in v:
        if i in a:
            del a[i]
print(sum(a.values()))
