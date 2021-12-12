from d10 import get_values

v = sorted(filter(None, get_values(True, {'(': 1, '[': 2, '{': 3, '<': 4})))
print(v[(len(v)) // 2])
