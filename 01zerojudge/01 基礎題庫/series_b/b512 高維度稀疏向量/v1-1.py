# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b512. 高維度稀疏向量


def to_dict(s: str) -> dict:
    return dict(map(lambda x: tuple(map(int, x.split(':'))), s.split()))


vector1 = to_dict(input())
vector2 = to_dict(input())

del vector1[0]
del vector2[0]

product = 0
for i in vector1:
    if i in vector2:
        product += vector1[i] * vector2[i]

print(product)
