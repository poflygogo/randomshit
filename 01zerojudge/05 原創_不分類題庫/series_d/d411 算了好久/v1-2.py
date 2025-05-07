# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d411. 算了好久......


def is_divisible_by_the_power_of_two(a: str, b: int) -> bool:
    if a[-1] not in {'0', '2', '4', '6', '8'}:
        return False
    if int(a[-b:]) % pow(2, b) == 0:
        return True
    return False


def main():
    while True:
        try:
            a, b = input().rstrip().split()
            print(
                f'YA!!終於算出{a}可被2的{b}次整除了!!' if is_divisible_by_the_power_of_two(a.lstrip('0'), int(b)) else
                f'可惡!!算了這麼久{a}竟然無法被2的{b}次整除')
        except EOFError:
            break


if __name__ == '__main__':
    main()
