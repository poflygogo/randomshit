# python 3.12
# UVa 665 False coin
# ZeroJudge c095

from typing import NamedTuple


# 只是為了可讀性
class Test(NamedTuple):
    lft: list
    rgt: list
    flag: int


def solve(arr: list[Test], total_num: int) -> int:
    def is_possible(t: Test, id: int, status: int) -> bool:
        w_lft = status * (id in t.lft)
        w_rgt = status * (id in t.rgt)
        r = -1 if w_lft < w_rgt else 0 if w_lft == w_rgt else 1
        return r == t.flag

    res = []
    for i in range(1, total_num + 1):
        if all(is_possible(t, i, -1) for t in arr) or all(is_possible(t, i, 1) for t in arr):
            res.append(i)

    if len(res) == 1:
        return res[0]
    else:
        return 0


def main():
    for test_case in range(int(input())):
        input()  # blank line
        n, m = map(int, input().split())
        arr = []
        for _ in range(m):
            p, *w = map(int, input().split())
            flag = input().strip()
            arr.append(Test(w[:p], w[p:], -1 if flag == "<" else 0 if flag == "=" else 1))
        if test_case:
            print()
        print(solve(arr, n))


main()
