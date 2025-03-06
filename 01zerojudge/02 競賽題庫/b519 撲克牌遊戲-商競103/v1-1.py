# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b519. 撲克牌遊戲-商競103


for _ in range(int(input())):
    cards = list(map(lambda x: int(x) - 1, input().split()))
    cards_counter = {}
    for i in range(5):
        n = cards[i]
        cards[i] = (n % 13, n // 13, n)
        cards_counter[n % 13] = cards_counter.get(n % 13, 0) + 1
    cards.sort()
    cards_counter_value = sorted(cards_counter.values())
    max_card_counter = max(cards_counter_value)

    # 鐵支(四條)
    if max_card_counter == 4:
        print(6)
    
    elif max_card_counter == 3:
        # 葫蘆
        if 2 in cards_counter_value:
            print(5)
        # 三條
        else:
            print(3)
    
    elif max_card_counter == 2:
        # two pair 兩對
        if cards_counter_value.count(2) == 2:
            print(2)
        # 一對
        else:
            print(1)
    
    elif (cards[4][0] - cards[0][0] == 4) or ([i[0] for i in cards] == [0, 9, 10, 11, 12]):
        # 同花
        if all(i[1] == cards[0][1] for i in cards):
            print(7)
        # 順子
        else:
            print(4)
    
    # 雜牌
    else:
        print(0)
