# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b837. 104北二1費氏數列
# 104北二區桃竹苗基資訊學科能力複賽


from bisect import bisect_left


def generate_fibonacci_sequence(n):
    result = [0, 1, 1]
    while result[-1] < n:
        result.append(result[-1] + result[-2])
    return result


def get_range_idx(a: int, b: int, fibonacci_sequence: list):
    if a > b:
        a, b = b, a
    idx_a = bisect_left(fibonacci_sequence, a)
    idx_b = bisect_left(fibonacci_sequence, b)
    if fibonacci_sequence[idx_b] == b:
        idx_b += 1
    return idx_a, idx_b


def main():
    fib_list = generate_fibonacci_sequence(1000000)
    t = int(input())
    result = [get_range_idx(*map(int, input().split()), fib_list) for _ in range(t)]
    print('\n------\n'.join('\n'.join(map(str, fib_list[a:b] + [b - a])) for a, b in result))


if __name__ == '__main__':
    main()
