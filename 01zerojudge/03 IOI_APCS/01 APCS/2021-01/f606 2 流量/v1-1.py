# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f606. 2. 流量
# 2021-01 APCS


def calc(iterator, data, n, m):
    # 紀錄每個城市有哪些 server
    city = {}
    for i in range(n):
        city[iterator[i]] = city.get(iterator[i], []) + [i]

    # 紀錄每個城市的總流量費用
    result = []
    for key, value in city.items():
        for j in range(m):
            flow = sum(data[i][j] for i in value)
            result.append(
                flow     if key == j     else 
                flow * 3 if flow <= 1000 else 
                (flow - 1000) * 2 + 3000
            )
    return sum(result)


def main():
    n, m, k = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(n)]
    cost = [calc(tuple(map(int, input().split())), data, n, m) for _ in range(k)]
    print(min(cost))
    

if __name__ == '__main__':
    main()
