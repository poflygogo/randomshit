from sys import stdin


for data in stdin:
    data = map(int, data.strip().split())
    print(sum(data))
