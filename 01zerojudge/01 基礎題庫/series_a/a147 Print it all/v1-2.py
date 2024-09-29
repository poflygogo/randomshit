from sys import stdin


for num in stdin:
    num = int(num)
    if num == 0: break
    print(*[i for i in range(0, num) if i % 7])
