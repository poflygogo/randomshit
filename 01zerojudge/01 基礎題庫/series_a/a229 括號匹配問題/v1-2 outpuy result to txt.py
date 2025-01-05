# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a229. 括號匹配問題
# dfs, backtrack


from sys import stdin, stdout


def main():
    test_cases = list(range(1, 14))
    ans = '\n\n'.join([bracket_match(i) for i in test_cases]) + '\n'
    with open(r'01zerojudge\01 基礎題庫\series_a\a229 括號匹配問題\result.txt', 'w', encoding='utf-8') as f:
        f.write(ans)


def bracket_match(n: int):
    def backtrack(lft: int, rgt: int, comb: list):
        if lft == rgt == 0:
            ans.append(comb.copy())
            return
        if lft > 0:
            backtrack(lft - 1, rgt, comb + ['('])
        if rgt > lft:
            backtrack(lft, rgt - 1, comb + [')'])

    ans = []
    backtrack(n, n, [])
    return '\n'.join(''.join(i) for i in ans)


if __name__ == '__main__':
    main()
    # test_case = (1, 2, 3, 4)
    # for i in test_case:
    #     print(bracket_match(i), end='\n\n')
