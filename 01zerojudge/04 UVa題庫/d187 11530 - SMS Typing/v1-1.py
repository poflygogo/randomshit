# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11530 SMS Typing
# ZeroJudge d187

key = {
    'a': 1, 'd': 1, 'g': 1, 'j': 1, 'm': 1, 'p': 1, 't': 1, 'w': 1, ' ': 1,
    'b': 2, 'e': 2, 'h': 2, 'k': 2, 'n': 2, 'q': 2, 'u': 2, 'x': 2,
    'c': 3, 'f': 3, 'i': 3, 'l': 3, 'o': 3, 'r': 3, 'v': 3, 'y': 3,
    's': 4, 'z': 4
}

for case in range(1, int(input()) + 1):
    print(f'Case #{case}: {sum(key[i] for i in input())}')
