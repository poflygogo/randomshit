# -*- encoding: utf-8 -*-
# python 3.12
# Zerojudge b520
# 103學年度商業類程式設計競賽模擬題


for _ in range(int(input())):
    num_reward = set(map(int, input().replace(' ', '').split(',')))
    num_guess = set(map(int, input().replace(' ', '').split(',')))

    result = num_reward.intersection(num_guess)
    print(len(result))
