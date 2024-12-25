from math import trunc
from utils import obj_list

def combo(n):
    if n in range(0, 4):
        return n
    elif n in range(4, 7):
        return registers[n - 4]
    return None

def div(i, o):
    registers[i] = trunc(registers[0] / (2 ** combo(o)))

def run(instruction, operand):
    if instruction == 0:
        div(0, operand)
    elif instruction == 1:
        registers[1] ^= operand
    elif instruction == 2:
        registers[1] =  combo(operand) % 8
    elif instruction == 3 and registers[0] != 0:
        return operand
    elif instruction == 4:
        registers[1] ^= registers[2]
    elif instruction == 5:
        out.append(int(combo(operand) % 8))
    elif instruction == 6:
        div(1, operand)
    elif instruction == 7:
        div(2, operand)
    return None

[registers, program] = obj_list(17)
registers = [int(r.split(' ')[-1]) for r in registers.split('\n')]
program = [int(n) for n in program.split(' ')[-1].split(',')]
program = [tuple(program[i:i+2]) for i in range(0, len(program), 2)]
out = []
i = 0
while i < len(program):
    instruction, operand = program[i]
    jump = run(instruction, operand)
    if jump is not None:
        i = jump
    else:
        i += 1
print(','.join(map(str, out)))
