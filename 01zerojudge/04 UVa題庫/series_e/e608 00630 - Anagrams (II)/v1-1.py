# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00630 Anagrams (II)
# ZeroJudge e608


t = int(input())
words = {}
for test in range(t):
    input()
    for _ in range(int(input())):
        text = input()
        words[text] = sorted(text)
    text = input()
    while text != 'END':
        text_sort = sorted(text)
        result = [i for i in words if words[i] == text_sort]
        print(f'Anagrams for: {text}')
        if result:
            print('\n'.join(f'  {i + 1}) {j}' for i, j in enumerate(result)))
        else:
            print(f'No anagrams for: {text}')
        text = input()
        if test < t - 1:
            print()
    words.clear()
