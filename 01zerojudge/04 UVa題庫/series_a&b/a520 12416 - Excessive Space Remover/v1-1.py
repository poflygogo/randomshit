# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12416 Excessive Space Remover
# ZeroJudge a520


def space_romover(s):
    cnt = 0
    while '  ' in s:
        s = s.replace('  ', ' ')
        cnt += 1
    return cnt


def main():
    while True:
        try:
            s = input()
        except EOFError:
            break
        print(space_romover(s))


if __name__ == '__main__':
    main()
