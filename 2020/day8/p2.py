from common import computer
with open('puzzle.in', 'r') as f:
    c = computer.Computer(f.read().splitlines())
    print(c.update_until_fixed())
