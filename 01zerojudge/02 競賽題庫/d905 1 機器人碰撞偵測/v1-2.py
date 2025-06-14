# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d905. 1. 機器人碰撞偵測
# 99學年度北基區資訊學科能力競賽


n, m = int(input()), int(input())
bot_curr = {}   # dict[str, int|bool]
for _ in range(m):
    id, x, y, d = map(int, input().split())
    bot_curr[id] = {'x': x, 'y': y, 'd': d, 'active': True}

bot_prev = bot_curr.copy()
direction = {1: (0, -1), 2: (1, -1), 3: (1, 0), 4: (1, 1),
             5: (0, 1), 6: (-1, 1), 7: (-1, 0), 8: (-1, -1)}

collision = {}  # dict[tuple[int], int], {發生碰撞的機器人: 碰撞時間}
time = 1        # 紀錄當前時間
while any(bot_curr[i]['active'] for i in bot_curr):
    # 所有機器人同時移動
    for i in bot_curr:
        if bot_curr[i]['active']:
            bot_curr[i]['x'] += direction[bot_curr[i]['d']][0]
            bot_curr[i]['y'] += direction[bot_curr[i]['d']][1]
            # 若下次移動會超出範圍，將 "active" 設置為 False
            if ((not 0 < bot_curr[i]['x'] + direction[bot_curr[i]['d']][0] <= n) or 
                (not 0 < bot_curr[i]['y'] + direction[bot_curr[i]['d']][1] <= n)):
                bot_curr[i]['active'] = False

    # 判斷是否碰撞
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

# 需要根據字典序輸出，故先 sort 再遍歷
if collision:
    print('\n'.join(f'{" ".join(map(str, i))},{collision[i]}' for i in sorted(collision)))
else:
    print('No collision!')
