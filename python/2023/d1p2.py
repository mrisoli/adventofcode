import re
from utils import str_list
from d1 import two_digits

number_mapping = {
        'one': '1ne',
        'two': '2wo',
        'three': '3hree',
        'four': '4our',
        'five': '5ive',
        'six': '6ix',
        'seven': '7even',
        'eight': '8ight',
        'nine': '9ine',
}

keys='|'.join(number_mapping.keys())
c = '(?=(' + keys + '))'

def str_to_int(s):
    for i in re.findall(c, s):
        s = s.replace(i, number_mapping[i])
    return s

two_digits(map(str_to_int, str_list(1)))
