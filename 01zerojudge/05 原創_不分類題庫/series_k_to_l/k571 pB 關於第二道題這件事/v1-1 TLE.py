# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k571. pB. 關於第二道題這件事


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    result = 0
    for i in range(n - k):
        cnt = 1 if arr[i] != 2 else 0
        for j in range(i + 1, n):
            if arr[j] != 2:
                cnt += 1
            if cnt > k:
                break
        else:
            j += 1
        result = max(result, j - i)

    print(result)


main()
