# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10063 Knuth's Permutation
# ZeroJudge a469


def knuth_permutation(token: list, path: list, idx: int = 0):
    if idx == len(token):
        print(''.join(path))
        return
    for i in range(len(path) + 1):
        path.insert(i, token[idx])
        knuth_permutation(token, path, idx + 1)
        path.pop(i)


def main():
    is_first_case = True
    while True:
        try:
            token = input()
        except EOFError:
            break
        if is_first_case:
            is_first_case = False
        else:
            print()
        knuth_permutation(list(token), [])


if __name__ == '__main__':
    main()
