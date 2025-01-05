# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a229. 括號匹配問題
# dfs, backtrack


from sys import stdin, stdout


def main():
    ipt = stdin.read().splitlines()
    stdout.write('\n\n'.join([bracket_match(int(i)) for i in ipt]) + '\n')


def bracket_match(n: int):
    def backtrack(lft: int, rgt: int, comb: list):
        if lft < 0 or rgt < 0 or lft > rgt:
            return
        if lft == rgt == 0:
            ans.append(comb.copy())
            return
        backtrack(lft - 1, rgt, comb + ['('])
        backtrack(lft, rgt - 1, comb + [')'])

    ans = []
    backtrack(n, n, [])
    return '\n'.join(''.join(i) for i in ans)


if __name__ == '__main__':
    main()
    # test_case = (1, 2, 3, 4)
    # for i in test_case:
    #     print(bracket_match(i), end='\n\n')
