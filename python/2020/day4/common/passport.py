from functools import reduce
from itertools import groupby
import re

REQ_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

class Passport:

    def __init__(self, p):
        self.passport = dict(map(lambda e: e.split(':'), p.split(' ')))

    def has_req(self):
        return 1 if len(REQ_FIELDS.difference(set(self.passport.keys()))) == 0 else 0

    def byr(self):
        return 1920 <= int(self.passport['byr']) <= 2002

    def iyr(self):
        return 2010 <= int(self.passport['iyr']) <= 2020

    def eyr(self):
        return 2020 <= int(self.passport['eyr']) <= 2030

    def hgt(self):
        n, s = re.match(r'(\d+)(\w+)', self.passport['hgt']).groups()
        n = int(n)
        return 150 <= n <= 193 if s == 'cm' else 59 <= n <= 76

    def hcl(self):
        return re.match(r'^#[0-9a-f]{6}$', self.passport['hcl'])

    def ecl(self):
        return self.passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

    def pid(self):
        return self.passport['pid'].isdigit() and len(self.passport['pid']) == 9

    def all_valid_fields(self):
        return self.byr() and self.iyr() and self.eyr() and self.hgt() and self.hcl() and self.ecl() and self.pid()

class PassportList:


    def __init__(self, n):
        with open(n) as f:
            ps = list(' '.join(list(g)) for k,g in groupby(f.read().splitlines(), key=lambda x: x != '') if k)
            self.passports = [Passport(p) for p in ps]

    def count_valid(self):
        return reduce(lambda x, y: x + y.has_req(), self.passports, 0)

    def is_valid(self, p):
        return 1 if p.has_req() and p.all_valid_fields() else 0

    def count_valid_data(self):
        return reduce(lambda x, y: x + self.is_valid(y), self.passports, 0)
