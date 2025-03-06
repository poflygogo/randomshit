# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b533. P21數學問題-集合


for _ in range(int(input())):
    text = input().strip()
    idx = text.index('}')
    set_a, set_b = set(map(int, text[1:idx].split(', '))), set(map(int, text[idx + 4:-1].split(', ')))
    
    a = set_a.union(set_b)
    b = set_a.intersection(set_b)
    c = set_a.difference(set_b)
    d = a - b
    
    result = [a, b, c, d]
    print(', '.join(f'{{{", ".join(map(str, sorted(i)))}}}' if i else 'N' for i in result))
