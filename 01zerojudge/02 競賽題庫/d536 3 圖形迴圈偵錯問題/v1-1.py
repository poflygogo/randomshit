# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d536. 3. 圖形迴圈偵錯問題
# 98學年度北基區資訊學科能力競賽


def main():
    graph = {}
    for _ in range(int(input())):
        a, b = input().strip()
        if a in graph:
            graph[a].add(b)
        else:
            graph[a] = {b}

    # 執行多次 bfs 尋找環
    result = float("inf")
    for node in graph.keys():
        dist = find_shortest_cycle(graph, node)
        if dist and dist < result:
            result = dist

    if result == float("inf"):
        print(0)
    else:
        print(result)


def find_shortest_cycle(graph: dict, start: str):
    distance = {start: 0}
    queue = [(start, 0)]
    while queue:
        node, step = queue.pop(0)
        step += 1
        for next_node in graph.get(node, []):
            # 第一個發現的環就是最短路徑，直接返回其路徑
            if next_node == start:
                return step
            if next_node not in distance:
                distance[next_node] = step
                queue.append((next_node, step))

    # no cycle
    return None


main()
