# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00454 Anagrams
# ZeroJudge e607


from collections import defaultdict


def anagrams(arr: list):
    result = defaultdict(list)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i][1] == arr[j][1]:
                result[arr[i][0]].append(arr[j][0])
    return '\n'.join(f'{i} = {j}' for i in result for j in result[i])


def counter(text: str):
    result = defaultdict(int)
    for i in text:
        if i .isalpha():
            result[i] += 1
    return result


def main():
    t = int(input())
    input()
    arr = []
    for i in range(t):
        while True:
            try:
                text = input()
            except EOFError:
                break
            if not text:
                break
            arr.append((text, counter(text)))
        print(anagrams(arr), end='\n\n' if i < t - 1 else '\n')


if __name__ == '__main__':
    main()
