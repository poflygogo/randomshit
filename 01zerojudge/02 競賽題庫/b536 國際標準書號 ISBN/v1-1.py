# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b536. 國際標準書號 ISBN


def is_valid_isbn(text: str) -> bool:
    text = text.replace('-', '')
    
    # ISBN 10
    if len(text) == 10:
        weight = tuple(range(10, 1, -1))
        s = sum(int(text[i]) * weight[i] for i in range(9))
        m = s % 11
        n = 11 - m
        if n == 10:
            return text[-1] == 'X'
        if n == 11:
            return text[-1] == '0'
        return text[-1] == str(n)
    
    # ISBN 13
    else:
        weight = (1, 3)
        s = sum(int(text[i]) * weight[i % 2] for i in range(12))
        m = s % 10
        n = 10 - m
        if n == 10:
            return text[-1] == '0'
        return text[-1] == str(n)


def main():
    for _ in range(int(input())):
        if is_valid_isbn(input().rstrip()):
            print('T')
        else:
            print('F')


if __name__ == '__main__':
    main()
