from sys import stdin, stdout

for num in stdin:
    num = int(num.strip())
    stdout.write(f'{1 + num * (num - 1) / 2:.0f}\n')