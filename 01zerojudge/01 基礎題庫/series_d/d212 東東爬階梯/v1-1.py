# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d212. 東東爬階梯


def main():
    dp    = [0] * 101
    dp[1] = 1
    dp[2] = 2

    for i in range(3, 101):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    while True:
        try:
            print(dp[int(input())])
        except:
            break


if __name__ == '__main__':
    main()
