stone = input().split()
stone_set = set(stone)
for i in stone_set:
    if stone.count(i) % 3:
        print(i)
        break
