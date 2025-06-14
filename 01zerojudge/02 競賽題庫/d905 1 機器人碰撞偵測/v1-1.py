# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d905. 1. 機器人碰撞偵測
# 99學年度北基區資訊學科能力競賽


n, m = int(input()), int(input())
bot_curr = {}

for _ in range(m):
    id, x, y, d = map(int, input().split())
    bot_curr[id] = {'x': x, 'y': y, 'd': d, 'active': True}

bot_prev = bot_curr.copy()
direction = {1: (0, -1), 2: (1, -1), 3: (1, 0), 4: (1, 1),
             5: (0, 1), 6: (-1, 1), 7: (-1, 0), 8: (-1, -1)}

collision = {}
time = 1
while any(bot_curr[i]['active'] for i in bot_curr):
    for i in bot_curr:
        if 0 < bot_curr[i]['x'] <= n and 0 < bot_curr[i]['y'] <= n:
            bot_curr[i]['x'] += direction[bot_curr[i]['d']][0]
            bot_curr[i]['y'] += direction[bot_curr[i]['d']][1]
        else:
            bot_curr[i]['active'] = False
        
    for i in bot_curr:
        temp = {i}
        for j in bot_prev:
            if j not in temp and bot_curr[i]['x'] == bot_prev[j]['x'] and bot_curr[i]['y'] == bot_prev[j]['y']:
                temp.add(j)
        if len(temp) < 2:
            continue
        temp = tuple(sorted(temp))
        if collision.get(temp, float('inf')) > time:
            collision[temp] = time
    bot_prev = bot_curr.copy()
    time += 1

if collision:
    print('\n'.join(f'{" ".join(map(str, i))},{collision[i]}' for i in sorted(collision)))
else:
    print('No collision!')
