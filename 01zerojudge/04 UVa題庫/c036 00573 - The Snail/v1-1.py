from sys import stdin


for line in stdin:
    target, up, down, fatigue = map(float, line.strip().split())
    if target == up == down == fatigue == 0.0: break

    fatigue = up * fatigue / 100    # 常量, 疲勞因子
    place, day = 0.0, 1               # 位置, 天數

    flag = True                     # 檢查是否成功, 預設為成功 True
    while True:
        place += up                 # 往上爬
        if place > target:         # 若達到目標代表成功
            break
        
        place -= down               # 往下滑
        if place < 0:              # 若回原點代表失敗
            flag = False
            break

        if up > fatigue:
            up -= fatigue
        else:
            up = 0
        day += 1
    
    print(
        f'{"success" if flag else "failure"} on day {day}'
        )
