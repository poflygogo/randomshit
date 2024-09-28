from sys import stdin


stdin.readline()
[print(i) for i in sorted(stdin.readlines(), key=lambda x: [int(i) for i in x.strip().split()])]
