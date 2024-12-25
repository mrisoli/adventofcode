from utils import obj_list

BUFSIZE = 100
MAX_LEN = 16

# Registers
reg_A = 0
reg_B = 0
reg_C = 0

# Buffers
in_buffer = []
out_buffer = []

ipc = 0
in_len = 0
out_len = 0

def parse_input(buffer):
    """Parse input buffer to initialize the input array."""
    global in_buffer, in_len
    buffer = buffer.split("Program: ")[1]
    in_buffer = [int(buffer[i]) for i in range(0, len(buffer), 2)]
    in_len = min(len(in_buffer), MAX_LEN)

def combo(operand):
    if operand in [0, 1, 2, 3]:
        return operand
    elif operand == 4:
        return reg_A
    elif operand == 5:
        return reg_B
    elif operand == 6:
        return reg_C
    else:
        raise AssertionError("Invalid operand")

def opcode_adv(operand):
    global reg_A
    reg_A >>= combo(operand)

def opcode_bdv(operand):
    global reg_B
    reg_B = reg_A >> combo(operand)

def opcode_cdv(operand):
    global reg_C
    reg_C = reg_A >> combo(operand)

def opcode_bxl(operand):
    global reg_B
    reg_B ^= operand

def opcode_bst(operand):
    global reg_B
    reg_B = combo(operand) & 7

def opcode_jnz(operand):
    global ipc
    if reg_A != 0:
        ipc = operand

def opcode_bxc(_):
    global reg_B
    reg_B ^= reg_C

def opcode_out(operand):
    global out_buffer, out_len
    out_buffer.append(combo(operand) & 7)
    out_len += 1

def next_opcode():
    global ipc
    ipc += 1
    return in_buffer[ipc - 1]

def run():
    global ipc
    opcode = next_opcode()
    operand = next_opcode()

    if opcode == 0:
        opcode_adv(operand)
    elif opcode == 1:
        opcode_bxl(operand)
    elif opcode == 2:
        opcode_bst(operand)
    elif opcode == 3:
        opcode_jnz(operand)
    elif opcode == 4:
        opcode_bxc(operand)
    elif opcode == 5:
        opcode_out(operand)
    elif opcode == 6:
        opcode_bdv(operand)
    elif opcode == 7:
        opcode_cdv(operand)
    else:
        raise AssertionError("Invalid opcode")

def eval_program(a):
    global reg_A, reg_B, reg_C, ipc, out_len, out_buffer
    reg_A, reg_B, reg_C = a, 0, 0
    ipc = 0
    out_len = 0
    out_buffer = []

    while ipc < in_len:
        run()

    return out_buffer[0]

def dfs(in_pos, curr):
    if in_pos < 0:
        return curr

    curr <<= 3
    target = in_buffer[in_pos]

    for i in range(8):
        n = curr + i
        if eval_program(n) == target:
            out = dfs(in_pos - 1, n)
            if out >= 0:
                return out

    return -1

[_, buffer] = obj_list(17)
parse_input(buffer)
result = dfs(in_len - 1, 0)
print(result)
