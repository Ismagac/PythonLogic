# Example 1:

# Input:
# x = 5
# Output: 2

# Example 2:

# Input:
# x = 4
# Output: 2

import math


def squareRoot(x):
    x = int(x)
    # pow(x, 0.5)
    return math.floor(math.sqrt(x))


print(squareRoot(5))
print(squareRoot(4))