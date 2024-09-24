from sys import stdin
import re


def record():
    _a, _b, _direction = case.strip().split()
    _a, _b = int(_a), int(_b)
    return _b, _a, _direction


def move():
    global x, y, prev_x, prev_y
    prev_x, prev_y = x, y
    
    step = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
    temp = direction // 45
    x += step[temp][0]
    y += step[temp][1]


# 初步處理資料
row, col = map(int, stdin.readline().strip().split())
mapinfo = [stdin.readline().strip() for _ in range(row)]
stdin.readline()

# 處理多筆 case 到 EOF 為止
flag = False
drop = []
for case in stdin:
    # 檢查是否已經到過傳送點
    if flag:
        stdin.readline()
        print("I think I don't need to move anymore.")
        continue
    
    # 紀錄座標, 方向
    x, y, direction = record()
    prev_x, prev_y = x, y
    direction = (
            0 if direction == 'N'
            else 45 if direction == 'NE'
            else 90 if direction == 'E'
            else 135 if direction == 'SE'
            else 180 if direction == 'S'
            else 225 if direction == 'SW'
            else 270 if direction == 'W'
            else 315
        )

    actions = re.findall(r'\D|\d+', stdin.readline().strip())
    # 行動
    for i, item in enumerate(actions):
        # 如果是數字就跳過(前一次循環已處理過)
        if item.isdigit():
            continue

        if item == 'M':
            move()

            # 移動後若掉到坑裡
            if not (0 < x <= row) or not (0 < y <= col) or mapinfo[x - 1][y - 1] == 'H':

                # 若這個坑已經踩過則忽視
                if (x, y, direction) in drop:
                    x, y = prev_x, prev_y
                    continue
                
                # 沒有掉過的坑、角度，就結束循環，輸出上一步的結果
                else:
                    drop.append((x, y, direction))
                    print(prev_y, prev_x, ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')[direction // 45], 'BAD PLAN!')
                    break
            
            # 移動後若踩到傳送點
            elif mapinfo[x - 1][y - 1] == 'T':
                flag = True
                print(y, x, 'FINISHED!')
                break

        elif item == 'R':
            direction = (direction + int(actions[i + 1])) % 360
        
        else:
            direction = (direction + 360 - int(actions[i + 1])) % 360
    
    # 所有行動執行完，途中沒有遇到任何特殊情況
    else:
        print(y, x, ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')[direction // 45])
