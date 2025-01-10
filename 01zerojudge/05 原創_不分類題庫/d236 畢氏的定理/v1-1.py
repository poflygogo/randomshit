# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d236. 畢氏的定理


def find():
    for a in range(2, 998):
        for b in range(a + 1, 998):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c


if __name__ == '__main__':
    print(find())
