# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e179. Runningman - 目標金額


from itertools import combinations


class Result:
    succeed: str = "YES"
    fail: str = "NO"


def is_possible(arr: list, k: int, target: int):
    for i in combinations(arr, k):
        if sum(i) == target:
            return True
    return False


def main():
    while True:
        try:
            n, k, target = map(int, input().split())
            arr = list(map(int, input().split()))
            if is_possible(arr, k, target):
                print(Result.succeed)
            else:
                print(Result.fail)
        except EOFError:
            break


main()
