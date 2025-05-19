# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i207. 檔名排序

# Sorting for Humans : Natural Sort Order | coding horror
# https://blog.codinghorror.com/sorting-for-humans-natural-sort-order/

# Ned Batchelder’s Compact Python Human Sort
# https://web.archive.org/web/20071217042318/http://nedbatchelder.com/blog/200712.html#e20071211T054956

import re

convert = lambda text: int(text) if text.isdigit() else text.upper()
natsort = lambda key: [convert(i) for i in re.split(r'\d+', key)]

data = [input() for _ in range(int(input()))]
data.sort(key=natsort)
print('\n'.join(data))

