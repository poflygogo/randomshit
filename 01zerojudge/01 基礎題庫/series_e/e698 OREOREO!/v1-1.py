# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e698. OREOREO!


def oreo(pattern: str, o_width: int, o_thick: int, r_width: int, r_thick: int, o: str, r: str):
    pattern = pattern.replace('RE', ' ')
    indentation = abs(o_width - r_width) // 2
    cookie = (' ' * indentation * (o_width < r_width) + o * o_width + '\n') * o_thick
    butter = (' ' * indentation * (o_width > r_width) + r * r_width + '\n') * r_thick
    return ''.join(cookie if i == 'O' else butter for i in pattern)


def main():
    from sys import stdin
    scan = stdin.readline

    for line in stdin:
        o_width, o_thick = map(int, line.rstrip().split())
        r_width, r_thick = map(int, scan().rstrip().split())
        o, r = scan().rstrip().split()
        n = int(scan().rstrip())
        for _ in range(n):
            print(oreo(scan().rstrip(), o_width, o_thick, r_width, r_thick, o, r))


if __name__ == '__main__':
    main()
