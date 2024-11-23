# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a627. 7. RAID Sizer
# HP CodeWars 2007


from math import ceil


disk = ((750, 250), (500, 140), (400, 110), (250, 75))

while True:
    try:
        require, raid = map(int, input().split())
    except EOFError:
        break
    else:
        cost = []
        if raid == 0:
            for i, j in disk:
                cnt = ceil(require / i)
                if cnt > 8:
                    break
                cost.append((i, j, cnt, cnt * j))
        
        elif raid == 1:
            for i, j in disk:
                cnt = ceil(require / i) * 2
                if cnt > 8:
                    break
                cost.append((i, j, cnt, cnt * j))

        else:   # if raid == 5
            for i, j in disk:
                cnt = ceil(require / i) + 1
                if cnt > 8:
                    break
                cost.append((i, j, cnt, cnt * j))
        
        cheap = min(cost, key=lambda x: x[3])
        disk_array = ({0: lambda x, y: x * y, 1: lambda x, y: x * y // 2, 5: lambda x, y: x * (y - 1)}[raid])(cheap[0], cheap[2])
        print(
            f'Qty: {cheap[2]} Disk: {cheap[0]}GB Price: ${cheap[1]}',
            f'Total price of this {disk_array}GB array: ${cheap[3]}',
            sep='\n',
            end='\n\n'
        )
