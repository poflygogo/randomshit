# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n632. 熱門商品 (Commodity)
# 2024-04 TOI 練習賽 新手組 第一題


from collections import Counter

k, n = map(int, input().split())
products = Counter(map(int, input().split()))
input()
shop = {i: sum(products[j] for j in map(int, input().split())) for i in range(n)}

print(
    max(products, key=lambda x: products[x]),
    min(shop, key=lambda x: shop[x]) + 1
)
