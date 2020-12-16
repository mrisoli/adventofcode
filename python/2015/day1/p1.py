with open('puzzle.in')  as f:
    s = f.read()
    print(s.count('(') - s.count(')'))
