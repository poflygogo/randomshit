# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d371. 3. Huffman 編碼中的編碼效能問題
# 96學年度全國資訊學科能力競賽


n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
result = sum((i + 1) * j for i, j in enumerate(arr[:-1]))
result += arr[-1] * (n - 1)
print(result)
