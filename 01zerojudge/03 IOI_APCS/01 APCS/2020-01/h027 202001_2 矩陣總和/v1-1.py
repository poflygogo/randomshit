# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge h027. 202001_2 矩陣總和
# 2020-01 APCS


def main():
    s, t, n, m, r = map(int, input().split())
    arr_a = [tuple(map(int, input().split())) for _ in range(s)]
    arr_b = [tuple(map(int, input().split())) for _ in range(n)]
    print(*matrix_sum(s, t, n, m, r, arr_a, arr_b), sep='\n')


def matrix_sum(ra, ca, rb, cb, r, arr_a, arr_b):
    count, min_diff = 0, float('inf')
    arr_a_sum = sum(arr_a[i][j] for i in range(ra) for j in range(ca))
    for row in range(rb - ra + 1):
        for col in range(cb - ca + 1):
            diff_cnt = arr_b_sum = 0
            for i in range(ra):
                for j in range(ca):
                    arr_b_sum += arr_b[row + i][col + j]
                    if arr_a[i][j] != arr_b[row + i][col + j]:
                        diff_cnt += 1
            if diff_cnt <= r:
                min_diff = min(min_diff, abs(arr_b_sum - arr_a_sum))
                count += 1

    if min_diff == float('inf'):
        min_diff = -1
    return count, min_diff


if __name__ == '__main__':
    main()
