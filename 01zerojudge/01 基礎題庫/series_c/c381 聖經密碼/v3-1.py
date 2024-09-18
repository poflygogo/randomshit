from sys import stdin, stdout

for line in stdin:
    n, m = map(int, line.split())
    if n == m == 0:
        break

    data = ''.join([stdin.readline().strip() for _ in range(n)])
    result = [data[int(key) - 1] for key in stdin.readline().strip().split()]

    stdout.write(f'{"".join(result)}\n')