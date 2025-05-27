# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j244. 111北二3a.兌獎問題
# 111北二區桃竹苗資訊學科能力複賽


def main():
    _, n = map(int, input().split())
    targets = [input() for _ in range(3)]
    arr = [input() for _ in range(n)]
    print(sum(max(judge(i, j) for j in targets) for i in arr))


def judge(n: str, target: str) -> int:
    if n == target:
        return 500_000
    if n.endswith(target[2:]):
        return 10_000
    if n.endswith(target[4:]):
        return 1_000
    if n.endswith(target[-3:]):
        return 300
    return 0


main()
