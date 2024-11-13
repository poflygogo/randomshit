from sys import stdin
from statistics import median


numbers = []
for num in stdin:
    numbers.append(int(num.rstrip()))
    print(int(median(numbers)))
