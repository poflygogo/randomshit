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
    result = max(len(data[0]) - 1, len(data[-1]) - 1, *[(len(data[i]) - 1) // 2 for i in range(1, len(data) - 1)])
    return result


if __name__ == '__main__':
    main()
