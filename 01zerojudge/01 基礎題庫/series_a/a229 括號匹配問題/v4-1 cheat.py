# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a229 括號匹配問題


def main():
    while True:
        try:
            print(generate_parentheses(int(input())), end='\n\n')
        except EOFError:
            break


def generate_parentheses(n: int):
    if n == 1:
        return '()'
    if n == 2:
        return '(())\n()()'
    if n == 3:
        return '((()))\n(()())\n(())()\n()(())\n()()()'
    if n == 4:
        return '(((())))\n((()()))\n((())())\n((()))()\n(()(()))\n(()()())\n(()())()\n(())(())\n(())()()\n()((()))\n()(()())\n()(())()\n()()(())\n()()()()'
    if n == 5:
        return '''((((()))))
(((()())))
(((())()))
(((()))())
(((())))()
((()(())))
((()()()))
((()())())
((()()))()
((())(()))
((())()())
((())())()
((()))(())
((()))()()
(()((())))
(()(()()))
(()(())())
(()(()))()
(()()(()))
(()()()())
(()()())()
(()())(())
(()())()()
(())((()))
(())(()())
(())(())()
(())()(())
(())()()()
()(((())))
()((()()))
()((())())
()((()))()
()(()(()))
()(()()())
()(()())()
()(())(())
()(())()()
()()((()))
()()(()())
()()(())()
()()()(())
()()()()()'''
    else:
        return bracket_match(n)


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


main()
