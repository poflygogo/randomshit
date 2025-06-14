# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b974. 3.任務二->誰是音樂達人


n, m = map(int, input().split())
score = {i: 0 for i in range(1, m + 1)}
for _ in range(n):
    ans, *arr = input().rstrip().split()
    for i in range(0, len(arr), 2):
        if arr[i + 1] == ans:
            score[int(arr[i])] += 1
            break

max_score = max(score.values())
print(' '.join(str(i) for i in range(1, m + 1) if score[i] == max_score))
print('\n'.join(f'{i} {score[i]}' for i in range(1, m + 1)))
