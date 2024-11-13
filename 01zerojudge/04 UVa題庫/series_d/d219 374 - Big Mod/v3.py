from sys import stdin

for line in stdin:
    if line.strip() == '': continue
    try:
        B = int(line.strip())
    except ValueError:
        B = int(line.replace(' ',''))
    P = int(stdin.readline().strip())
    M = int(stdin.readline().strip())

    print(pow(B, P, M))