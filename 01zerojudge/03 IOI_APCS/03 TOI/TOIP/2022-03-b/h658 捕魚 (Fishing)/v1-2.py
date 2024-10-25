ship_x, ship_y = map(int, input().split())
fish = [tuple(map(int, input().split())) for _ in range(int(input()))]
print(*min(fish, key=lambda x: (x[0] - ship_x) ** 2 + (x[1] - ship_y) ** 2))
