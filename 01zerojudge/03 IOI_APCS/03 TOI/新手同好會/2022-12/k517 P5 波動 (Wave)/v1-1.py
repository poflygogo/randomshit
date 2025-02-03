# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k517. P5.波動 (Wave)
# 2022-12 TOI 新手同好會


def calc(d, a, b) -> tuple:
    return (int(a)/int(b), d)


direction = {'W': 1, 'S': 2, 'E': 3, 'N': 4}
info = [calc(*input().split()) for _ in range(int(input()))]
info.sort(key=lambda x: (x[0], direction[x[1]]))
print(''.join(i[1] for i in info))
