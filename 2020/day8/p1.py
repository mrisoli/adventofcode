from common import computer
with open('puzzle.in', 'r') as f:
    c = computer.Computer(f.read().splitlines())
    c.run()
    print(c.acc)
