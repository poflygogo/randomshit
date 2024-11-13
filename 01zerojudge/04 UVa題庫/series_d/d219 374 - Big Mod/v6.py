from sys import stdin

for line in stdin:
    if line.strip() == '': continue

    try:
        B = int(line.strip())
        P = int(stdin.readline().strip())
        M = int(stdin.readline().strip())
    except ValueError:
        B, P, M = map(int, line.split())
    
    print(pow(B, P, M))