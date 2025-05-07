# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d448. 好熱好熱


def converter(t1, t2, t3, x1, x3):
    print(f'{(t2 * (x1 - x3)+ t1 * x3 - t3 * x1) / (t1 - t3):.6f}')


def main():
    while True:
        try:
            t1, t2, t3, x1, x3 = map(float, input().split())
            converter(t1, t2, t3, x1, x3)
        except EOFError:
            break


if __name__ == '__main__':
    main()
