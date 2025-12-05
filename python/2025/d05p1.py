from utils import obj_list

def parse_range(s):
    return list(map(int, s.split('-')))

def  is_fresh(ranges, ingredient):
    for [low, high] in ranges:
        if low <= ingredient <= high:
            return True
    return False

ranges, ingredients = obj_list(5)
ranges = list(map(parse_range, ranges.split('\n')))
ingredients = list(map(int, ingredients.split('\n')))
print(sum(1 for i in ingredients if is_fresh(ranges, i)))
