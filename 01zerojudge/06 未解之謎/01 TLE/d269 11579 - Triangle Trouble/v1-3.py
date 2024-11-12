# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11579 Triangle Trouble
# ZeroJudge d269

for _ in range(int(input())):
    sides = list(map(float, input().split()))   # 測資有可能出現不是整數的數字(?
    total_side = int(sides.pop(0))              # 每筆測資的第一個數字代表有幾個邊長要比較
    sides.sort()                                # 確保數字由小排到大

    area = []
    for a in range(2, total_side):
        for b in range(a - 1, 0, -1):
            for c in range(b - 1, 0, -1):
                if sides[a] >= sides[b] + sides[c]:
                    break

                # TODO: ...

                
    
    print(f'{max(area) ** 0.5 if area else 0.00:.2f}')
