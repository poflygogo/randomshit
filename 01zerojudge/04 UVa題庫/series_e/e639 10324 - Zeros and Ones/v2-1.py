# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10324 Zeros and Ones
# Zerojudge e639


def binary_search(n) -> int:
    lft, rgt = 0, len(trend)
    while lft < rgt:
        mid = (lft + rgt) // 2
        if trend[mid] == n:
            return mid
        if trend[mid] < n:
            lft = mid + 1
        else:
            rgt = mid
    return lft - 1


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
    
    trend = [0]
    trend.extend([i for i in range(1, len(text)) if text[i - 1] != text[i]])

    for _ in range(int(input())):
        a, b = sorted(map(int, input().split()))
        idx_a, idx_b = binary_search(a), binary_search(b)
        print('Yes' if idx_a == idx_b else 'No')

    # text = tuple(text)
    # trend = [0]
    # trend.extend([i for i in range(1, len(text)) if text[i - 1] != text[i]])
    # print(trend)
    # print([text[i] for i in trend])
