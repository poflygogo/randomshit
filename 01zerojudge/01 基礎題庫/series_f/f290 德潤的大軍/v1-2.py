# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f290. 德潤的大軍


n = int(input())
arr = tuple(map(int, input().split()))

data = {arr[0]: [arr[0]], arr[-1]: [arr[-1]]}
for i in range(1, n - 1):
    temp = arr[i - 1] + arr[i + 1]
    if temp not in data:
        data[temp] = []
    data[temp].append(arr[i])

print('\n'.join(f'{i} {j}' for i in sorted(data) for j in sorted(data[i])))
