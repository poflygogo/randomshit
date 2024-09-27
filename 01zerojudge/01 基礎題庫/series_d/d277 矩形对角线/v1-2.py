from sys import stdin


for num in stdin:
    print(int(num) >> 1 << 1)
