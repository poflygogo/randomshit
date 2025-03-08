# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b561. 1.披薩大小


def main():
    while True:
        try:
            _, *pizza1 = map(int, input().split())
            _, *pizza2 = map(int, input().split())
        except EOFError:
            break
        print(f'{abs(calc_pizza_size(pizza1) - calc_pizza_size(pizza2)):.2f}')


def calc_pizza_size(pizza: list) -> float:
    PI = 3.14159
    return sum((i / 2) ** 2 * PI for i in pizza)


if __name__ == '__main__':
    main()
