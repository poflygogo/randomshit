# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10252 Common Permutation
# ZeroJudge e507


from sys import stdin


def common_permutation(a: str, b: str) -> str:
    elements = set(a).intersection(set(b))
    a_counter = dict.fromkeys(elements, 0)
    b_counter = a_counter.copy()
    for i in a:
        if i in elements:
            a_counter[i] += 1
    for i in b:
        if i in elements:
            b_counter[i] += 1
    for i in elements:
        a_counter[i] = min(a_counter[i], b_counter[i])
    return ''.join(i * a_counter[i] for i in sorted(a_counter))


def main():
    while True:
        try:
            text1, text2 = (input() for _ in range(2))
        except EOFError:
            break
        print(common_permutation(text1, text2))


if __name__ == '__main__':
    main()
