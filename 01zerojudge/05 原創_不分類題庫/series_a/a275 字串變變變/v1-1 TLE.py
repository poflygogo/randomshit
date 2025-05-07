# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a275. 字串變變變


def is_possible_to_be_the_same(s1, s2):
    s1_counter = {}
    s2_counter = {}
    for i in s1:
        s1_counter[i] = s1_counter.get(i, 0) + 1
    for i in s2:
        s2_counter[i] = s2_counter.get(i, 0) + 1
    return bool(s1_counter == s2_counter)


def main():
    while True:
        text1 = input()
        if text1 == 'STOP!!':
            break
        text2 = input()
        print('yes' if is_possible_to_be_the_same(text1, text2) else 'no')


if __name__ == '__main__':
    main()
