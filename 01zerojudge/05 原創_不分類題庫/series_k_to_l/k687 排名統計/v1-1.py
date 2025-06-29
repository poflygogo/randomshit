# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k687. 排名統計


from re import findall

data = [findall(r"\d+|\D+", input()) + [i] for i in range(int(input()))]
data.sort(key=lambda x: (int(x[1]), -x[2]), reverse=True)

k = 1
print(f"1 {data[0][0]} {data[0][1]}")
for i in range(1, len(data)):
    if int(data[i][1]) < int(data[i - 1][1]):
        k += 1
    print(f"{k} {data[i][0]} {data[i][1]}")
