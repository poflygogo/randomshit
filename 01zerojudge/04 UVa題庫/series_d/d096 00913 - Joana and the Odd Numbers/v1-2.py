from sys import stdin


for num in stdin:
    num = int(num.rstrip())
    print(((1 + num) * ((num + 1) // 2) - 3) * 3)
    