# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j244. 111北二3a.兌獎問題
# 111北二區桃竹苗資訊學科能力複賽


def main():
    _, n = map(int, input().split())
    targets = [input() for _ in range(3)]
    targets = [{targets[j][i:] for j in range(3)} for i in (0, 2, 4, -3)]
    arr = [input() for _ in range(n)]
    print(sum(judge(i, targets) for i in arr))


def judge(n: str, target: list) -> int:
    if n in target[0]:
        return 500_000
    if n[2:] in target[1]:
        return 10_000
    if n[4:] in target[2]:
        return 1_000
    if n[-3:] in target[3]:
        return 300
    return 0


main()
