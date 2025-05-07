# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d336. 一即是全、全即是一


from sys import stdin, stdout


def is_multiple_of_three(num: str):
    """num is a binary number"""
    temp = sum(int(num[i]) for i in range(len(num) - 2, -1, -2)) - sum(int(num[i]) for i in range(len(num) - 1, -1, -2))
    return temp % 3 == 0


t, *binary_nums = stdin.read().splitlines()
stdout.write('\n'.join('Yes' if is_multiple_of_three(i.rstrip()) else 'No' for i in binary_nums) + '\n')
