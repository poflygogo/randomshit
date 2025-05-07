# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d456. 社辦合併


def string_slice(data: list, a: str, b: str, a_idx=None, b_idx=None) -> tuple:
    data_reversed = data[::-1]
    a_idx = data_reversed.index(a)
    b_idx = data_reversed.index(b)
    a_idx, b_idx = min(a_idx, b_idx), max(a_idx, b_idx)
    return (data_reversed[:a_idx + 1] + data_reversed[b_idx:])[::-1], data_reversed[a_idx + 1:b_idx][::-1]


def main():
    for _ in range(int(input())):
        data = input()
        a, b = list(input())
        result, data_popped = string_slice(data, a, b)
        print(result, data_popped, sep='\n')


if __name__ == '__main__':
    main()
