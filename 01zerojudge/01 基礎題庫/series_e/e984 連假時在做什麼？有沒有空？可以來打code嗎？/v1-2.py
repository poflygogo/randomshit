# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e984. 連假時在做什麼？有沒有空？可以來打code嗎？


from collections import deque

k = int(input())
arr = deque(range(1, 10))
for _ in range(k - 1):
    item = arr.popleft()
    if item % 10 != 0:
        arr.append(item * 10 + item % 10 - 1)
    arr.append(item * 10 + item % 10)
    if item % 10 != 9:
        arr.append(item * 10 + item % 10 + 1)
print(arr.popleft())
