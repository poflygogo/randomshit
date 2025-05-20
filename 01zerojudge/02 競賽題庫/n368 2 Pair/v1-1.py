# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n368. 2. Pair
# 112學年度新北新莊高中校內資訊學科能力競賽


arr = [max(*map(int, input().split()), 0) for _ in range(int(input()))]
arr.sort(reverse=True)

# prefix sum
for i in range(1, len(arr)):
    arr[i] += arr[i - 1]

print('\n'.join(map(str, arr)))
