# q672. pD. 帕拉迪島攻防戰
# 114學年度hgsh校內賽


from sys import stdin
from collections import defaultdict
import heapq


def titan(titan_info, graph):
    """
    args:
        n (int): n 個城鎮
        m (int): m 條可建立的雙向道路
        k (int): k 個有巨人的城鎮
        titan_info (tuple): 有巨人的城鎮清單
        graph (defaultdict): 所有城鎮彼此連通的成本
    return:
        int: 建立道路的最小成本
    """
    visited = set()
    total_cost = 0
    priority_queue = []

    visited.update(set(titan_info))
    for node in titan_info:
        for neighbor, cost in graph[node].items():
            heapq.heappush(priority_queue, (cost, node, neighbor))
    
    while priority_queue:
        cost, u, v = heapq.heappop(priority_queue)
        if v in visited or u not in visited:
            continue
        visited.add(v)
        total_cost += cost
        if v in graph:
            for n_neighbor, n_cost in graph[v].items():
                if n_neighbor not in visited:
                    heapq.heappush(priority_queue, (n_cost, v, n_neighbor))
    return total_cost


def main():
    _, titan_info, *data = stdin.read().splitlines()
    titan_info = tuple(map(int, titan_info.split()))
    graph = defaultdict(dict)
    for line in data:
        u, v, c = map(int, line.split())
        graph[u][v] = graph[v][u] = c
    print(titan(titan_info, graph))


main()
