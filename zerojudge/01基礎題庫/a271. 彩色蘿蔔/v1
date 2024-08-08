"""
x = 吃紅蘿蔔，體重 +x g, y = 吃白蘿蔔，體重 +y g
z = 吃黃蘿蔔，體重 -z g, w = 吃黑蘿蔔，體重 -w g
n = 吃黑蘿蔔後，每層中毒buff -n g(中毒當下不算)
m = 兔子初始體重 m g
---------------------------------------
0 = 不吃蘿蔔, 1 = 吃紅蘿蔔, 2 = 吃白蘿蔔
3 = 吃黃蘿蔔, 4 = 吃黑蘿蔔
---------------------------------------
早上會因為中毒先扣血，晚上才吃蘿蔔
輸出一段時間後的體重
如果兔子沒血了，就輸出bye~Rabbit
"""
for _ in range(int(input())):
    x, y, z, w, n, m = map(int,input().split())
    carrot = tuple(map(int, input().split()))
    is_dead = False
    poison_level = 0
    for eat in carrot:
        m -= n * poison_level
        if m <= 0:
            is_dead = True
            break
        if eat == 1: m += x
        elif eat == 2: m += y
        elif eat == 3: m -= z
        elif eat == 4:
            m -= w
            poison_level += 1
        if m <= 0:
            is_dead = True
            break
    print("bye~Rabbit") if is_dead else print(f"{m}g")
