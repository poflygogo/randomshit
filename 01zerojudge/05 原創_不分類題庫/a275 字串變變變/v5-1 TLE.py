# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a275. 字串變變變


from sys import stdin


def is_possible_to_be_the_same(s1, s2):
    ascii_s1 = sum(ord(c) for c in s1)
    ascii_s2 = sum(ord(c) for c in s2)
    return ascii_s1 == ascii_s2


def main():
    for text1 in stdin:
        text1 = text1.rstrip()
        if text1 == 'STOP!!':
            break
        text2 = next(stdin).rstrip()
        print('yes' if is_possible_to_be_the_same(text1, text2) else 'no')


if __name__ == '__main__':
    main()
