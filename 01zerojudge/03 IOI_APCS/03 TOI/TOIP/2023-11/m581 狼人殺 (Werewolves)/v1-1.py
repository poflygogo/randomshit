# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m581. 狼人殺 (Werewolves)
# 2023-11 TOI 練習賽 新手組 第一題


def main():
    input()
    players = list(map(int, input().split()))
    die = int(input())
    while die != 0:
        if players[die - 1] is not None:
            players[die - 1] = None
        else:
            print('Wrong')
            break
        die = int(input())

    else:
        if any(i == -1 for i in players):
            print('Werewolves')
        else:
            print('Townsfolk')

main()
