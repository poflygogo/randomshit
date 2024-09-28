from sys import stdin


stdin.readline()
data = stdin.readlines()
data.sort(key=lambda x: [int(i) for i in x.strip().split()])
for i in data:
    print(i)
