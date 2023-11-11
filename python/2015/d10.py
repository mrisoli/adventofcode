from utils import str_list
import re

def split_repeat_characters(input_string):
    groups = re.findall(r'((\w)\2*)', input_string)
    result = [(group[1], len(group[0])) for group in groups]
    return result

def look_and_say(r):
    i = str_list(10)[0]
    for _ in range(r):
        c = split_repeat_characters(i)
        i = ''
        for char, count in c:
            i += str(count) + char
    print(len(i))
