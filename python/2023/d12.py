def parse_line(line):
    springs, count = line.split(' ')
    count = tuple(map(int, count.split(',')))
    return springs,count
