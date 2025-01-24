# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b899. 2. 物品探測
# 2016 高雄市資訊學科能力複賽


def main():
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())
    c1, c2 = map(int, input().split())
    line_ab = (a1 - b1) ** 2 + (a2 - b2) ** 2
    line_ac = (a1 - c1) ** 2 + (a2 - c2) ** 2
    if line_ab > line_ac:
        print(a1 + b1 - c1, a2 + b2 - c2)
    elif line_ab < line_ac:
        print(a1 + c1 - b1, a2 + c2 - b2)
    else:
        print(b1 + c1 - a1, b2 + c2 - a2)


if __name__ == '__main__':
    main()
