from math import prod
from utils import str_list

def calc(col_strings):
    # Last row contains the operator
    *num_rows, op_row = col_strings
    op = op_row.strip()

    # Read each digit position top-to-bottom to form operands
    # The alignment is already in the column strings
    max_len = max(len(row) for row in num_rows)
    operands = []
    for pos in range(max_len):
        digits = [row[pos] for row in num_rows if pos < len(row) and row[pos] != ' ']
        if digits:
            operands.append(int(''.join(digits)))

    if op == '+':
        return sum(operands)
    return prod(operands)

def make():
    lines = str_list(6)
# Find the maximum line length
    max_len = max(len(line) for line in lines)

    # Pad all lines to the same length
    lines = [line.ljust(max_len) for line in lines]

    # Find columns that are all spaces (separators)
    separators = []
    for col in range(max_len):
        if all(line[col] == ' ' for line in lines):
            separators.append(col)

    # Extract column boundaries
    boundaries = []
    start = 0
    for sep in separators:
        if sep > start:
            boundaries.append((start, sep))
        start = sep + 1
    if start < max_len:
        boundaries.append((start, max_len))

    # Extract each column as a list of strings
    result = []
    for start, end in boundaries:
        col_strings = [line[start:end] for line in lines]
        # Skip empty columns
        if any(s.strip() for s in col_strings):
            result.append(col_strings)

    return result

f = make()
print(f)
print(sum(map(calc, f)))
