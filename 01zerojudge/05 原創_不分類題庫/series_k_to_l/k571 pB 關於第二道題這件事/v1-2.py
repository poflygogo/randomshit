# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k571. pB. 關於第二道題這件事


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    result = 0
    lft = 0
    cnt = 0
    for rgt in range(n):
        if arr[rgt] != 2:
            cnt += 1
            if cnt > k:
                while arr[lft] == 2:
                    lft += 1
                lft += 1
        result = max(result, rgt - lft + 1)

    print(result)


main()
