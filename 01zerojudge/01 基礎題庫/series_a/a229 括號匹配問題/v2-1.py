# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a229. 括號匹配問題
# code by chatGPT


from sys import stdin, stdout


def main():
    ipt = stdin.read().splitlines()
    stdout.write('\n\n'.join([bracket_match(int(i)) for i in ipt]) + '\n')


def bracket_match(n: int) -> str:
    def backtrack(lft: int, rgt: int, comb: list, results: list):
        if lft == 0 and rgt == 0:
            results.append(''.join(comb))
            return
        if lft > 0:
            comb.append('(')
            backtrack(lft - 1, rgt, comb, results)
            comb.pop()  # 回溯後移除
        if rgt > lft:
            comb.append(')')
            backtrack(lft, rgt - 1, comb, results)
            comb.pop()  # 回溯後移除

    results = []
    backtrack(n, n, [], results)
    return '\n'.join(results)


if __name__ == '__main__':
    main()
