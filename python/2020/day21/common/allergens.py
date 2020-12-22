import re
r_ing = re.compile(r'\w+\s')
def get_data(f):
    s = {}
    all_ings = {}
    for l in f:
        [ings, allergens] = l.split('(')
        allergens = allergens[9:-1]
        ings = list(map(lambda x: x.strip(), r_ing.findall(ings)))
        allergens = allergens.split(', ')
        for a in allergens:
            if a in s:
                s[a] = s[a].intersection(ings)
            else:
                s[a] = set(ings)
        for ing in ings:
            all_ings[ing] = all_ings.get(ing, 0) + 1
    return (s, all_ings)
