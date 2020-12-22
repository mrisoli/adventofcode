from common import allergens
def sort_by_key(el):
    return el[0]
f = open('p.in').read().splitlines()
(s, _) = allergens.get_data(f)
print(s)
counts = []
counted = set()
while len(counts) < len(s):
    for i,v in s.items():
        if len(v) == 1 and i not in counted:
            counts.append((i,v))
            counted.add(i)
            for j, kj in s.items():
                if i != j:
                    for el in v:
                        if el in kj:
                            kj.remove(el)

counts.sort(key=sort_by_key)
print(','.join(list(map(lambda x: list(x[1])[0], counts))))
