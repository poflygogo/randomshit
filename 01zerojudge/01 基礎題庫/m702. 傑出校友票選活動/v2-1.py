# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m702. 傑出校友票選活動


n, m = map(int, input().split())
counter = {}
for _ in range(n):
    text = input()
    counter[text] = counter.get(text, 0) + 1

print(' '.join(sorted(counter, key=lambda x: counter[x], reverse=True)[:m]))
