from sys import stdin

for line in stdin:
    if line.strip() == '': continue
    B = int(line.strip())
    P = int(stdin.readline().strip())
    M = int(stdin.readline().strip())

    print((B % M) ** P)