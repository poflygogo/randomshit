# q390. 113北二2a.爬梯遊戲
# 113北二區桃竹苗資訊學科能力複賽


from bisect import bisect_left


def ghost_leg(start: int, data: list) -> int:
    curr_side = start
    if not data[curr_side]:
        return curr_side + 1
    curr = data[curr_side][0]
    while True:
        curr_side += curr[1]
        next_idx = bisect_left(data[curr_side], (curr[0], -curr[1])) + 1
        if next_idx == len(data[curr_side]):
            break
        curr = data[curr_side][next_idx]
    return curr_side + 1


def main():
    data: list[list[tuple[int, int]]]
    a, b = map(int, input().split())
    data = [[] for _ in range(a)]
    for i in range(a - 1):
        tmp = list(map(int, input().split()))
        data[i    ].extend([(i,  1) for i in tmp])
        data[i + 1].extend([(i, -1) for i in tmp])
    for i in data:
        i.sort()
    result = [ghost_leg(i, data) for i in range(a)]
    result = [(j, i) for i, j in enumerate(result, start=1)]
    result.sort()
    print(*[i for _, i in result])


main()
