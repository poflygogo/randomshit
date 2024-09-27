from sys import stdin


for data in stdin:
    print(sum(int(i) for i in data.strip().split()))
