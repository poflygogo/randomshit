# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d422. 2.字串處理


def string_processing(s: str) -> str:
    result = []
    cnt = 0
    for i in range(len(s)):
        if s[i] == 'b':
            result.append(' ' * cnt)
            cnt = 0
        elif s[i] == '!':
            result.append('\n')
            cnt = 0
        elif s[i].isdigit():
            cnt += int(s[i])
        else:
            result.append(s[i] * cnt)
            cnt = 0
    return ''.join(result)


def main():
    while True:
        try:
            s = input().rstrip()
            print(string_processing(s))
        except EOFError:
            break


if __name__ == '__main__':
    main()
