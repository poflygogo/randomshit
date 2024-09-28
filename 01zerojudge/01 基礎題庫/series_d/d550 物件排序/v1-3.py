from sys import stdin


stdin.readline()
data = [[int(j) for j in i.strip().split()] for i in stdin]
data.sort()
for i in data:
    print(*i)
