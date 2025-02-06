# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c679. 大家來出題 { 2: hello, World }


import random


w, v1, v2 = map(int, input().split())
seen = set()
n = iter(range(v1, v2 + 1))
for _ in range(w):
    target_length  = next(n)
    if target_length == v2:
        n = iter(range(v1, v2 + 1))
    text = ''.join(chr(random.randrange(97, 123)) for _ in range(target_length))
    while text in seen:
        text = ''.join(chr(random.randrange(97, 123)) for _ in range(target_length))
    seen.add(text)
    text = text.capitalize()
    print(f'{text}: hello, {text}')
