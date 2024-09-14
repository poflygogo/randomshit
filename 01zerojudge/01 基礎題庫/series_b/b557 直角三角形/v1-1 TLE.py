from sys import stdin


def get_triangles_total(length: int, lines: list) -> int:
    triangles = []
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                check = (lines[i], lines[j], lines[k])
                # 三角形定義: 兩條較短的邊長和必定大於最長的邊
                if check[0] + check[1] > check[2] and check[0] ** 2 + check[1] ** 2 == check[2] ** 2:
                    triangles.append(check)
    return len(triangles)


_ = next(stdin)
for num in stdin:
    num = int(num)
    data = sorted(map(int, next(stdin).strip().split()))
    print(get_triangles_total(num, data))
