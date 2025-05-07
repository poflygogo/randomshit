# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a275. 字串變變變


from sys import stdin
from collections import Counter


def is_possible_to_be_the_same(s1, s2):
    s1_counter = Counter(s1)
    s2_counter = Counter(s2)
    return bool(s1_counter == s2_counter)


def main():
    for text1 in stdin:
        text1 = text1.rstrip()
        if text1 == 'STOP!!':
            break
        text2 = next(stdin).rstrip()
        print('yes' if is_possible_to_be_the_same(text1, text2) else 'no')


if __name__ == '__main__':
    main()
