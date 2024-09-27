from sys import stdin


for num in stdin:
    num = int(num)
    if num & 1 == 0:
        print(num)
    else:
        print(int(num) - 1)
