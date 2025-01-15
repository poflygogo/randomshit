# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10063 Knuth's Permutation
# ZeroJudge a469


def knuth_permutation(token: list, path: list):
    if not token:
        print(''.join(path))
        return
    curr_token = token.pop(0)
    for i in range(len(path) + 1):
        knuth_permutation(token[:], path[:i] + [curr_token] + path[i:])


def main():
    while True:
        try:
            token = input()
        except EOFError:
            break
        knuth_permutation(list(token), [])
        print()


if __name__ == '__main__':
    main()
