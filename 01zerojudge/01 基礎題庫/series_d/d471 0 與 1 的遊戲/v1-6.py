from sys import stdin


for num in stdin:
    num = int(num)
    for i in range(2 << (num - 1)):
        print(f'{bin(i)[2:].zfill(num)}')
