from sys import stdin


stdin.readline()
data = [[int(j) for j in i.strip().split()] for i in stdin]
data.sort(key=lambda x: (x[0], x[1], x[2]))
for i in data:
    print(*i)
