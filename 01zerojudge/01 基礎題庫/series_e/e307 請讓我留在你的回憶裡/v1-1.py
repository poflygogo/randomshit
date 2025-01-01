# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e307. 請讓我留在你的回憶裡


from sys import stdin, stdout


def main():
    data = map(lambda x: x.replace('  ', ''), stdin.readlines())
    stdout.write(''.join(data))


if __name__ == '__main__':
    main()
