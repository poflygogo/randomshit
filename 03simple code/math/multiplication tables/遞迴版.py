# -*- encoding: utf-8 -*-
# python 3.12


def multiplication_table(num_pair: list[int], depth: int=2):
    if depth == 0:
        print(f'{num_pair[0]} * {num_pair[1]} = {num_pair[0] * num_pair[1]:>2d}')
        return
    for i in range(1, 10):
        num_pair.append(i)
        multiplication_table(num_pair, depth - 1)
        num_pair.pop()


if __name__ == '__main__':
    multiplication_table([])
