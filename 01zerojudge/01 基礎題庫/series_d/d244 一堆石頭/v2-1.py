stone = sorted(input().split())
for i in range(0, len(stone), 3):
    if stone[i] != stone[i + 2]:
        print(stone[i])
        break
