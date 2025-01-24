# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b899. 2. 物品探測
# 2016 高雄市資訊學科能力複賽


def main():
    a = complex(*map(int, input().split()))
    b = complex(*map(int, input().split()))
    c = complex(*map(int, input().split()))
    length_ab = abs(a - b)
    length_ac = abs(a - c)
    if length_ab > length_ac:
        print(int(a.real + b.real - c.real), int(a.imag + b.imag - c.imag))
    elif length_ab < length_ac:
        print(int(a.real + c.real - b.real), int(a.imag + c.imag - b.imag))
    else:
        print(int(b.real + c.real - a.real), int(b.imag + c.imag - a.imag))


if __name__ == '__main__':
    main()
