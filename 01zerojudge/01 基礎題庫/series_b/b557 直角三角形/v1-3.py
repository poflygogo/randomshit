from sys import stdin


def get_triangles_total(lines: list) -> int:
    def counter(to_count: list) -> dict:
        r = {}
        for i in to_count:
            r[i] = r.get(i, 0) + 1
        return r

    lines_counter = counter(lines)
    lines_keys = sorted(lines_counter.keys())
    length = len(lines_keys)
    result = 0
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                check = (lines_keys[i], lines_keys[j], lines_keys[k])
                # 三角形定義: 兩條較短的邊長和必定大於最長的邊
                if check[0] + check[1] > check[2] and check[0] ** 2 + check[1] ** 2 == check[2] ** 2:
                    result += lines_counter[check[0]] * lines_counter[check[1]] * lines_counter[check[2]]
    return result


_ = next(stdin)
for _ in stdin:
    data = sorted(map(int, next(stdin).strip().split()))
    print(get_triangles_total(data))
