# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import numpy as np

def sum_squares(limit: int) -> list:
    x = np.array(range(1, limit + 1))
    y = x ** 2
    return sum(y)

def square_sum(limit: int) -> list:
    return sum(range(1, limit + 1)) ** 2

print(abs(sum_squares(100) - square_sum(100)))