# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n688. pC. 卡牌遊戲


from bisect import bisect_left


def solve():
    _, k = map(int, input().split())
    arr = sorted(map(int, input().split()))

    # 二分搜查找 0 可以插入的位置，返回的值相當於所有負數的數量
    neg_cnt = bisect_left(arr, 0)

    # 將所有負數都轉換後，還剩餘多少元素需要轉換
    switch_left = k - neg_cnt

    # 不夠換 or 剛好換完
    if switch_left <= 0:
        print(sum(arr[neg_cnt:]) - sum(arr[:switch_left]) + sum(arr[k:neg_cnt]))

    # 全部都能換完，不保留任何負數
    elif switch_left % 2 != 0:
        print(sum(arr[neg_cnt:]) - sum(arr[:neg_cnt]))

    # 剩下一個負數
    else:
        print(sum(arr[neg_cnt:]) - sum(arr[: neg_cnt - 1]) + arr[neg_cnt - 1])


# solve()

if __name__ == "__main__":
    import test_case
    import io
    import sys

    cnt = 1
    for i in test_case.a:
        sys.stdin = io.StringIO(i.strip())
        print(f"----test {cnt}----")
        solve()
        cnt += 1
