# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a229. 括號匹配問題
# dp


from sys import stdin, stdout


def main():
    ipt = stdin.read().splitlines()
    stdout.write('\n\n'.join(['\n'.join(generate_parentheses(int(i))) for i in ipt]) + '\n')


def generate_parentheses(n):
    dp = [[] for _ in range(n + 1)]
    dp[0] = [""]

    for i in range(1, n + 1):
        for j in range(i):
            dp[i].extend(["(" + left + ")" + right for left in dp[j] for right in dp[i - j - 1]])
    dp[n].reverse()
    
    return dp[n]


if __name__ == '__main__':
    main()
    # print('\n\n'.join(['\n'.join(generate_parentheses(int(i))) for i in '1234']))
