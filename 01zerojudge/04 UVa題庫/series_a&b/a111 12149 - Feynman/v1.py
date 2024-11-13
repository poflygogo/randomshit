from sys import stdin, stdout

for n in stdin:
    n = int(n)
    if not n:
        break

    stdout.write(f'{n * (n + 1) * (2 * n + 1) / 6 :.0f}\n')