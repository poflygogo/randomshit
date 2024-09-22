from sys import stdin


n = int(stdin.readline().strip())           # 小便斗數量
urinal = [0 for _ in range(n)]              # 小便斗陣列
used = [0 for _ in range(n)]                # 剩餘使用時間
count = 0                                   # 有多少人正在使用廁所
for data in stdin:
    a, b = map(int, data.strip().split())   # a = 男生的編號, b = 該男生的如廁時間

    # 先讓正在如廁的人處理
    for i, item in enumerate(urinal):
        if item != 0:
            if used[i] in (0, 1):
                urinal[i] = 0
                used[i] = 0
                count -= 1
            else:
                used[i] -= 1
    
    # 檢查廁所是否有空位
    if count == n:
        flag = True
    
    else:
        flag = False
        
        # 找空位，先找兩側都為空的位置
        for i in range(n):
            if (i == 0 and urinal[i] == urinal[i - 1] == 0) or \
                (i == n - 1 and urinal[-1] == urinal[-2] == 0) or \
                (urinal[i] == urinal[i - 1] == urinal[i + 1] == 0):
                urinal[i] = a
                used[i] = b
                count += 1
                break
        
        # 找不到，有洞就隨便進
        else:
            for i, item in enumerate(urinal):
                if item == 0:
                    urinal[i] = a
                    used[i] = b
                    count += 1
                    break
        
    # 輸出廁所狀態
    if flag:
        print('  Not enough')
    
    print(
        f'Number: {" ".join(str(i) for i in urinal)}',
        f'  Time: {" ".join(str(i) for i in used)}',
        sep='\n',
        end='\n\n'
    )
