# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b562. 2.神奇的「負二進位表示法」


def main():
    while True:
        try:
            num = input()
        except EOFError:
            break
        print(base_neg2(num))


def base_neg2(num: str) -> int:
    k = 1
    result = 0
    for i in reversed(num):
        result += k * (i == '1')
        k *= -2
    return result


if __name__ == '__main__':
    main()
