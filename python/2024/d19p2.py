from utils import obj_list

def count_combinations(patterns, design):
    """
    Counts the number of possible combinations to construct the design using the patterns.

    :param patterns: List of pattern strings.
    :param design: The string design to be checked.
    :return: The number of possible combinations.
    """
    # Create a set for fast lookup
    patterns_set = set(patterns)

    # Dynamic programming table to store results
    dp = [0] * (len(design) + 1)
    dp[0] = 1  # One way to construct an empty string

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]

    return dp[-1]

patterns, designs = obj_list(19)
designs = designs.split('\n')
patterns = patterns.split(', ')

print(sum(count_combinations(patterns, design) for design in designs))
