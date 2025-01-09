# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10424 Love Calculator
# ZeroJudge n773


def main():
    while True:
        try:
            print(love_calculator(input().upper(), input().upper()))
        except EOFError:
            break


def love_calculator(name1: str, name2: str):
    num1 = sum(ord(i) - 64 for i in name1 if i.isalpha())
    num2 = sum(ord(i) - 64 for i in name2 if i.isalpha())

    while num1 > 9:
        num1 = sum(int(i) for i in str(num1))
    while num2 > 9:
        num2 = sum(int(i) for i in str(num2))
    
    if num1 > num2:
        num1, num2 = num2, num1
    return f'{num1 * 100 / num2: <.2f} %'


if __name__ == '__main__':
    main()
    a = 'saima'
    b = 'shanto'
    print(love_calculator(a.upper(), b.upper()))
