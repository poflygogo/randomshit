# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j538. 賣場設置 (Market)
# 2022-12 TOI 練習賽 新手組


category: str
products: list[int]
location: dict[str, list]

category = input().lower()
products = list(map(int, input()))

location = {}
for i in range(len(category)):
    if category[i] not in location:
        location[category[i]] = []
    location[category[i]].append(i)


for i in location:
    total = sum(products[j] for j in location[i])
    avg, exc = divmod(total, len(location[i]))
    
    for j in location[i]:
        products[j] = avg
    
    if exc:
        for j in location[i][-exc:]:
            products[j] += 1

print(''.join(map(str, products)))
