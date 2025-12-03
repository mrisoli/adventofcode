from utils import int_grid

TARGET_LENGTH = 12
def joltage(digits):
    n = len(digits)

    result = []

    digits_to_drop = n - TARGET_LENGTH

    for digit in digits:
        while result and result[-1] < digit and digits_to_drop > 0:
            result.pop()
            digits_to_drop -= 1

        result.append(digit)

    return int("".join(map(str, result[:TARGET_LENGTH])))

print(sum(map(joltage, int_grid(3))))
