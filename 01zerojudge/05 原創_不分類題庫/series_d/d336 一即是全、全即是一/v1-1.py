# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d336. 一即是全、全即是一


from sys import stdin, stdout


t, *binary_nums = stdin.read().splitlines()
stdout.write('\n'.join('Yes' if int(i, 2) % 3 == 0 else 'No' for i in binary_nums) + '\n')
