# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge l154. 走地圖(1)


def find_x():
    for r in range(size):
        for c in range(size):
            if graph[r][c] != "-":
                return c + 1, r + 1


size = int(input())
graph = [input().split() for _ in range(size)]
x, y = find_x()

total, succeed = 0, 0
while True:
    try:
        d, step = input().split()
        step = int(step)
        total += 1
        nx, ny = x, y

        if d == "right":
            nx = x + step
        elif d == "left":
            nx = x - step
        elif d == "up":
            ny = y - step
        elif d == "down":
            ny = y + step

        if (0 < nx <= size) and (0 < ny <= size):
            succeed += 1
            x, y = nx, ny
            print(f"x{x} y{y}")
        else:
            print(-1)
    except EOFError:
        break

fail = total - succeed
ratios = succeed * 100 / total
if ratios.is_integer():
    ratios = int(ratios)
else:
    ratios = round(ratios, 1)
print(f"最終坐標為x{x} y{y}", f"{total}/{succeed}/{fail}/{ratios}%", sep="\n")
