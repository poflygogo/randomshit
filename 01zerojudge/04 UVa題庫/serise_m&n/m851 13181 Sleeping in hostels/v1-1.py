# -*- encoding: utf-8 -*-
# python 3.12
# UVa 13181 Sleeping in hostels
# ZeroJudge m851


def main():
    while True:
        try:
            line = input().rstrip()
        except EOFError:
            break
        print(sleeping_in_hotels(line))


def sleeping_in_hotels(data: str) -> int:
    data = data.split('X')
    if len(data) == 1:
        return len(data[0] - 1)
    result = 0
    for i in range(len(data)):
        if i in (0, len(data) - 1):
            result = max(len(data[i]) - 1, result)
        else:
            result = max(len(data[i]) // 2 - (len(data[i]) % 2 == 0), result)
    return result


if __name__ == '__main__':
    main()
