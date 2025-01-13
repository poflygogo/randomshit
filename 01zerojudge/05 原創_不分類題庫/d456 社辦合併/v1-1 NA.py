# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d456. 社辦合併


def string_slice(data: list, a: str, b: str) -> tuple:
    a_idx = data.index(a)
    b_idx = data.index(b)
    a_idx, b_idx = min(a_idx, b_idx), max(a_idx, b_idx)
    return data[:a_idx + 1] + data[b_idx:], data[a_idx + 1:b_idx]


def main():
    for _ in range(int(input())):
        data = input()
        a, b = list(input())
        result, data_popped = string_slice(data, a, b)
        print(result, data_popped, sep='\n')


if __name__ == '__main__':
    main()
