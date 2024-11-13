# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11233 Deli Deli
# ZeroJudge e368


L, N = map(int, input().split())
special = {i:j for i, j in [input().split() for _ in range(L)]}

for _ in range(N):
    text = input().rstrip()
    if text in special:
        print(special[text])
        continue

    if text[-1] == 'y' and text[-2] not in {'a', 'e', 'i', 'o', 'u'}:
        print(text[:-1] + 'ies')
    
    elif text[-1] in {'o', 's', 'x'} or text[-2:] in {'ch', 'sh'}:
        print(text + 'es')
    
    else:
        print(text + 's')
