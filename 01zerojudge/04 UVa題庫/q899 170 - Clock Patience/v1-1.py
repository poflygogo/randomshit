# -*- encoding: utf-8 -*-
# python 3.12
# UVa 170 - Clock Patience
# ZeroJudge q899


def main():
    while True:
        ipt = input().strip()
        if ipt == "#":
            break
        cards = [ipt.split()]
        cards.extend([input().split() for _ in range(3)])

        # 旋轉陣列
        cards.reverse()
        for i in cards:
            i.reverse()
        cards = list(map(list, zip(*cards)))

        print(*clock_patience(cards), sep=",")


card_value = {str(i): i - 1 for i in range(2, 10)}
card_value.update({"A": 0, "T": 9, "J": 10, "Q": 11, "K": 12})


def clock_patience(cards: list, curr: int = 12):
    # 直接模擬
    cnt = 1
    item = cards[curr].pop()
    curr = card_value[item[0]]
    while cards[curr]:
        item = cards[curr].pop()
        curr = card_value[item[0]]
        cnt += 1
    return cnt, item


main()
