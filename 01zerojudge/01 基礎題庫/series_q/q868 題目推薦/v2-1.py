# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q868. 題目推薦


from collections import defaultdict

data = defaultdict(set)
for _ in range(int(input())):
    a, b = map(int, input().split())
    data[a].add(b)


def is_connected(s: int, e: int) -> bool:
    if s == e:
        return True
    queue = [s]
    seen = set(queue)
    while queue:
        s = queue.pop(0)
        for i in data.get(s, set()):
            if i == e:
                return True
            if i not in seen:
                queue.append(i)
                seen.add(i)
    return False


print("Yay" if is_connected(*map(int, input().split())) else "Come on")
