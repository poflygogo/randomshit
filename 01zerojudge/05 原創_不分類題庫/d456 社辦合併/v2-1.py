# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d456. 社辦合併


def string_slice(data: list, a: str, b: str, a_idx=None, b_idx=None) -> tuple:
    for i in range(len(data) -1, -1, -1):
        if a_idx is not None and b_idx is not None:
            break
        if a_idx is None and data[i] == a:
            a_idx = i
        if b_idx is None and data[i] == b:
            b_idx = i
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
