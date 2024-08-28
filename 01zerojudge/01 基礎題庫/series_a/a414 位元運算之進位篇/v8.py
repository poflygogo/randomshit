from sys import stdin

for num in stdin:
    num = bin(int(num))
    if num == '0b0':
        break

    print(len(num) - len(num.rstrip("1")))