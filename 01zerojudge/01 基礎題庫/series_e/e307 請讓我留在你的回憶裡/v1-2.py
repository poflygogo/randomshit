# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e307. 請讓我留在你的回憶裡


from sys import stdin


def main():
    for line in stdin:
        line = line.rstrip()
        print(line.replace('  ', ''))


if __name__ == '__main__':
    main()
