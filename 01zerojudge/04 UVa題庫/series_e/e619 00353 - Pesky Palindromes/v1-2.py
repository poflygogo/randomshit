# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00353 Pesky Palindromes
# ZeroJudge e619


while True:
    try:
        text = input()
    except EOFError:
        break
    else:
        length = len(text)
        p = set()   # p: palindromes
        for i in range(length):
            for j in range(i + 1, length + 1):
                temp = text[i:j]
                if temp in p:
                    continue
                if all(temp[k] == temp[-1 - k] for k in range((j - i) // 2 + 1)):
                    p.add(temp)
        print(f"The string '{text}' contains {len(p)} palindromes.")
