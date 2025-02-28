# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d157. 序章-永夜抄-B


from sys import stdin

TOTAL_PLAYER = 3
PLAYER = ('十六夜', '紅美鈴', '帕秋莉·諾雷姬')
END = ('繼續做家事', '趕上旅程')

symbol = {'Scissors': 0, 'Stone': 1, 'Paper': 2}
result = {i: 0 for i in PLAYER}
game = 0
for choices in stdin:
    game += 1
    choices = choices.rstrip()
    if choices == 'End':
        break
    
    if choices == 'Game Over':
        print('\n'.join(f'{i}總計贏了{result[i]}局比賽' for i in PLAYER))
        continue

    choices = choices.split(',')
    counter = {i: 0 for i in range(TOTAL_PLAYER)}
    winner = None
    for i in range(TOTAL_PLAYER):
        if choices[i] not in symbol:
            winner = i
            break
        choices[i] = symbol[choices[i]]
        counter[choices[i]] += 1
    
    if winner is not None:
        result[PLAYER[i]] += 1
        print(f'{PLAYER[i]}贏了第{game}局的比賽')
        continue

    if 0 not in counter.values() or TOTAL_PLAYER in counter.values():
        print(f'第{game}局不分勝負')
        continue

    other, target, _ = sorted(counter, key=lambda x: counter[x], reverse=True)
    if (target + 1) % 3 == other:
        target = choices.index(target)
        for i in range(TOTAL_PLAYER):
            if i != target:
                result[PLAYER[i]] += 1
        print(f'{PLAYER[target]}輸了第{game}局的比賽')
    else:
        target = choices.index(target)
        result[PLAYER[target]] += 1
        print(f'{PLAYER[target]}贏了第{game}局的比賽')

print(END[max(result, key=lambda x: result[x]) == PLAYER[0]])
