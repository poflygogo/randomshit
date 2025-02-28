# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d155. 序章-永夜抄-A


PLAYER = ('紫', '靈夢')
symbol = {'Scissors': 0, 'Stone': 1, 'Paper': 2}
counter = {0: 0, 1: 0}  # key 對應的是 PLAYER 的 index，不過這邊其實用 list 應該就可以了

text = input()
while text != 'Game Over':
    a, b = map(lambda x: symbol[x], text.split())
    flag = (a + 1) % 3 == b
    counter[flag] += 1
    print(f'{PLAYER[flag]}獲勝')
    text = input()
print(('螢火的蹤跡', '悲慘的籌措起香油錢')[counter[1] > counter[0]])
