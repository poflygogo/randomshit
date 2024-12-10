# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10324 Zeros and Ones
# Zerojudge e639


# 實在是不確定到底是 eof 為止還是空字串為止
cases = 0
while True:
    try:
        text = input().rstrip()
    except EOFError:
        break

    if not text:
        break

    cases += 1
    print(f'Case {cases}:')
    for _ in range(int(input())):
        i, j = sorted(map(int, input().split()))
        print('Yes' if all(text[i] == text[k] for k in range(i + 1, j + 1)) else 'No')
