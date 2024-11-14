# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10056 What is the Probability?
# ZeroJudge e510


for _ in range(int(input())):
    player_total, probability, player_id = input().rstrip().split()

    # 若機率為 0，無人可成功，直接輸出 0.000
    probability = float(probability)
    if probability == 0:
        print('0.0000')
        continue

    player_total = int(player_total)
    player_id = int(player_id)

    # 套用等比級數公式
    q = 1  - probability
    print(f'{(pow(q, player_id - 1) * probability) / (1 - pow(q, player_total)):.4f}')
