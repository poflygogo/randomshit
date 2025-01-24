# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a275. 字串變變變


from sys import stdin


def is_possible_to_be_the_same(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_counter = {}
    for i in s1:
        s1_counter[i] = s1_counter.get(i, 0) + 1
    for i in s2:
        if i not in s1_counter or s1_counter[i] == 0:
            return False
        s1_counter[i] -= 1
    return all(i == 0 for i in s1_counter.values())


def main():
    for text1 in stdin:
        text1 = text1.rstrip()
        if text1 == 'STOP!!':
            break
        text2 = next(stdin).rstrip()
        print('yes' if is_possible_to_be_the_same(text1, text2) else 'no')


if __name__ == '__main__':
    main()
