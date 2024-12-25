from utils import obj_list

def can_construct(patterns, design):
    """
    Checks if the design can be constructed using the patterns.

    :param patterns: List of pattern strings.
    :param design: The string design to be checked.
    :return: True if the design can be constructed, otherwise False.
    """
    # Create a set for fast lookup
    patterns_set = set(patterns)

    # Dynamic programming table to store results
    dp = [False] * (len(design) + 1)
    dp[0] = True  # Empty string can always be constructed

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] = dp[i] or dp[i - len(pattern)]

    return dp[-1]
patterns, designs = obj_list(19)
designs = designs.split('\n')
patterns = patterns.split(', ')

print(sum(can_construct(patterns, design) for design in designs))
