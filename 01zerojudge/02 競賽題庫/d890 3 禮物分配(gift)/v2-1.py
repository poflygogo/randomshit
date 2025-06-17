# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d890. 3.禮物分配(gift)
# 99學年度台北市資訊學科能力競賽


n, k = map(int, input().split())
gift = [int(input()) for _ in range(n)]
total = sum(gift)


if total < k * 2:
    result2 = k
    result1 = total - result2
    print(f"{result1} {result2}")

elif total % 2 == 1:
    total -= 1
    print(f"{total // 2} {total // 2 + 1}")

else:
    print(f"{total // 2} {total // 2}")
