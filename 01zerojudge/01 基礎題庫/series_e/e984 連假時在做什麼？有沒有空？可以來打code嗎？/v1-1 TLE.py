# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e984. 連假時在做什麼？有沒有空？可以來打code嗎？


k = int(input())
dequeue = list(range(1, 10))
for _ in range(k - 1):
    item = dequeue.pop(0)
    if item % 10 != 0:
        dequeue.append(item * 10 + item % 10 - 1)
    dequeue.append(item * 10 + item % 10)
    if item % 10 != 9:
        dequeue.append(item * 10 + item % 10 + 1)
print(dequeue[0])
