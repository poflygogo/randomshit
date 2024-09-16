from sys import stdin, stdout

for line in stdin:
    row, col = map(int, line.strip().split())
    data = [stdin.readline().strip().split() for _ in range(row)]
    [stdout.write(f'{" ".join([data[j][i] for j in range(row)])}\n') for i in range(col)]