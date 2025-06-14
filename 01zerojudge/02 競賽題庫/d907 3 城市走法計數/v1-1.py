# -*- encoding: utf-8 -*-
# python 3.6
# ZeroJudge d907. 3. 城市走法計數
# 99學年度北基區資訊學科能力競賽

# 87 zerojudge 還在用 python 6，想用完整的型別註釋得 import 這玩意兒
from typing import Dict, List, Set


def main():
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    graph = make_graph(n, matrix)
    city1 = int(input())
    city2 = int(input())
    step = int(input())
    print(counting_total_possible_paths(graph, city1 - 1, city2 - 1, step + 1))
    print(*find_not_connection(n, graph), sep='\n')


def make_graph(n: int, matrix: List[List[int]]) -> Dict[int, Set[int]]:
    result = {} # Dict[int, Set[int]]
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                result.setdefault(i, set()).add(j)
                result.setdefault(j, set()).add(i)
    return result


def counting_total_possible_paths(graph: Dict[int, Set[int]], city1: int, city2: int, step: int):
    if step == 0:
        return city1 == city2
    total_path = 0
    for i in graph[city1]:
        total_path += counting_total_possible_paths(graph, i, city2, step - 1)
    return total_path


def find_not_connection(n: int, graph: Dict[int, Set[int]]):
    def bfs(start: int, target: int):
        queue = [start]
        seen = set(queue)
        while queue:
            node = queue.pop(0)
            for i in graph[node]:
                if i == target:
                    return True
                elif i not in seen:
                    seen.add(i)
                    queue.append(i)
        return False

    for i in range(n):
        for j in range(n):
            if i != j and not bfs(i, j):
                return i + 1, j + 1
    return 0, 0


main()
