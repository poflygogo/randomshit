"""
Write a Python program that fills an array T with n integers (S < n <= 10) between 1 and 20.
Then the program calculates and displays the sum, product, and arithmetic mean of the elements in T.

What is S? Is it 5?
"""

from functools import reduce
from random import randint
from operator import mul


while True:
    try:
        n = int(input("Enter a number n. (5 < n <= 10) -> "))
    except ValueError:
        print('Please enter a real number.')
    else:
        if not (5 < n <= 10):
            print('Number out of range. Please enter a number between 5 and 10.')
        else:
            break

T: list[int] = [randint(1, 20) for _ in range(n)]
print(
    '------Result------',
    f'T      : {" ".join(map(str, T))}',
    f'Sum    : {sum(T)}',
    f'Product: {reduce(mul, T)}',
    f'Mean   : {sum(T) / n: <.1f}',
    sep='\n'
)
