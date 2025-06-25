# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q877. 國文&程式?!


# ---------------------------------------------------

import sys
import io
Q = """
3
公子光之父曰諸樊
諸樊弟三人，次曰餘祭，次曰夷眛，次曰季子札
夷眛之子曰僚
公子光 僚
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


IS_FATHER = "之父曰"
IS_SON = "之子曰"

graph = {}
age_order = {}
for _ in range(int(input())):
    text = input()
    if IS_FATHER in text:
        a, b = text.split(IS_FATHER)
        graph[a] = b
    elif IS_SON in text:
        b, a = text.split(IS_SON)
        graph[a] = b
    else:
        eldest, *temp = text.split("，次曰")
        eldest = eldest[:eldest.index("弟")]
        father = graph.get(eldest, None)
        age_order[father] = [eldest] + temp
        for i in age_order[father]:
            graph[i] = father

def get_depth(start, depth: int=0):
    if start not in graph:
        return depth
    return get_depth(graph[start], depth + 1)

a, b = input().split()
a_depth = get_depth(a)
b_depth = get_depth(b)

if a_depth < b_depth:
    print(a)
elif a_depth > b_depth:
    print(b)
elif graph[a] == graph[b]:
    print(min(a, b, key=lambda x: age_order[graph[x]].index(x)))
else:
    print(min(a, b, key=lambda x: age_order[graph[graph[x]]].index(graph[x])))
