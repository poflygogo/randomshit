# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n689. pD. 技能點數


class Skill:
    # 紀錄每個節點的資料
    # 也可以直接不這樣寫，但很難讀...
    def __init__(self):
        self.pre = []  # 上游節點
        self.next = []  # 下游節點
        self.unlock = False  # 是否已解鎖


# 把資料讀進來，初步處理
n, m, k = map(int, input().split())
skill_book = list(map(int, input().split()))

graph = [Skill() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].next.append(v)
    graph[v].pre.append(u)

for i in skill_book:
    graph[i].unlock = True


cnt = k
queue = skill_book.copy()
while queue:
    skill_id = queue.pop(0)

    # 若該節點尚未解鎖，代表曾走過，但當時不確定結果
    # 現在又遇到它了，檢查看看是否要繼續走
    # 若現在可以解鎖就將 unlock 設置為 True 並前往下一個節點
    # 若依然不行，則直接跳過，不再處理，反正未來會有其他節點走到這
    if not graph[skill_id].unlock:
        if all(graph[i].unlock for i in graph[skill_id].pre):
            graph[skill_id].unlock = True
            cnt += 1
        else:
            continue

    for i in graph[skill_id].next:
        # 如果是已經解鎖的節點，代表在其他時候就已經確認可以通行，直接跳過
        if graph[i].unlock:
            continue

        # 檢查所有前置技能是否已解鎖
        if all(graph[j].unlock for j in graph[i].pre):
            graph[i].unlock = True
            cnt += 1

        # 無論是否成功習得技能都先加到佇列中
        queue.append(i)


print(cnt)
