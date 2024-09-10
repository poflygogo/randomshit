from sys import stdin


data = tuple(map(int, stdin.readlines()))
for num in data:
    print((num ** 3 + 5 * num + 6) // 6)
