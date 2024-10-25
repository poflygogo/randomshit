ship_x, ship_y = map(int, input().split())
fish = {}
for _ in range(int(input())):
    fish_x, fish_y = map(int, input().split())
    fish[(fish_x, fish_y)] = (ship_x - fish_x) ** 2 + (ship_y - fish_y) ** 2
print(*min(fish, key=lambda x: fish[x]))
