from itertools import chain
from utils import obj_list

def parse_range(s):
    return list(map(int, s.split('-')))

def merge_ranges(ranges):
      if not ranges:
          return []
      merged = [ranges[0]]
      for current in ranges[1:]:
          last = merged[-1]
          if current[0] <= last[1]:
              merged[-1] = [last[0], max(last[1], current[1])]
          else:
              merged.append(current)
      return merged

ranges, _ = obj_list(5)
ranges = list(map(parse_range, ranges.split('\n')))
ranges = merge_ranges(sorted(ranges, key=lambda x: x[0]))
print(sum(h - l + 1 for l,h in ranges))
