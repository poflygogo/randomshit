from sys import stdin, stdout
from itertools import accumulate

stdin.readline()
data = list(map(int, stdin.readline().split()))

prefix_sum = [0]
prefix_sum.extend(list(accumulate(data)))

stdin.readline()
for line in stdin:
    num1, num2 = map(int, line.split())
    output = f'{prefix_sum[num2] - prefix_sum[num1 - 1]}\n'
    stdout.write(output)