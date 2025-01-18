# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e948. 基礎代謝率 (BMR Calculation)
# 2019-03 TOI 練習賽 新手組


def bmi(gender: int, age: int, hight: int, weight: int) -> float:
    if gender == 1:
        return (
            weight * 13.7 +
            hight * 5.0 -
            age * 6.8 +
            66
        )
    else:
        return (
            weight * 9.6 +
            hight * 1.8 -
            age * 4.7 +
            655
        )


def main():
    for _ in range(int(input())):
        print(f'{bmi(*map(int, input().split())): .2f}')


if __name__ == '__main__':
    main()
