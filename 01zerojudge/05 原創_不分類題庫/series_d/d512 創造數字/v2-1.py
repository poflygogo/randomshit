# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d512. 創造數字


def create_number(length: int, nums: tuple):
    # 初始化 dp，0 表示沒有選中任何數字時的狀態
    dp = {0}
    for num in nums:
        dp.update({x + num for x in dp})
    return len(dp) - 1


def main():
    while True:
        try:
            n = int(input())
            nums = tuple(map(int, input().split()))
            print(create_number(n, nums))
        except EOFError:
            break


if __name__ == '__main__':
    main()
