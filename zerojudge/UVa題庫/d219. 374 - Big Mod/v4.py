from sys import stdin

for line in stdin:
    if line.strip() == '': continue

    B = int(line.strip().replace(' ',''))
    P = int(stdin.readline().strip().replace(' ',''))
    M = int(stdin.readline().strip().replace(' ',''))

    print(pow(B, P, M))