# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k862. 輩份比較


graph = {}
for _ in range(int(input())):
    a, b = input().split()
    graph[a] = b


def steps_to_root(x: str, cnt: int = 0) -> int:
    if x not in graph:
        return cnt
    return steps_to_root(graph[x], cnt + 1)


a, b = input().split()
print(steps_to_root(b) - steps_to_root(a))
