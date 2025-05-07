from sys import stdin


result = 0
for _ in range(int(stdin.readline().strip()) - 1):
    result ^= int(next(stdin).strip())

print(result)
