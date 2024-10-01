from sys import stdin


for line in stdin:
    a, b = line.rstrip().split()
    if a + b != b + a:
        print('= =')
    else:
        while len(a) > 0:
            a, b = b, a.replace(b, '')
        print(b)
