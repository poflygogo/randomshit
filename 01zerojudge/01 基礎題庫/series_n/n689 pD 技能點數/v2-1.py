# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n689. pD. 技能點數


# 拓樸排序
class Skill:
    # 紀錄每個節點的資料
    # 也可以直接不這樣寫，但很難讀...
    def __init__(self):
        self.next = []  # 下游節點
        self.degree = 0 # 入度 in-degree


# 把資料讀進來，初步處理
n, m, k = map(int, input().split())
skill_book = list(map(int, input().split()))

graph = [Skill() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].next.append(v)
    graph[v].degree += 1


for i in skill_book:
    graph[i].degree = -1

cnt = k
queue = skill_book.copy()
while queue:
    skill_id = queue.pop(0)
    for i in graph[skill_id].next:
        graph[i].degree -= 1
        if graph[i].degree == 0:
            queue.append(i)
            cnt += 1

print(cnt)
