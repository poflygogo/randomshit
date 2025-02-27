# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11342 - Three-square
# ZeroJudge d188


from math import sqrt, floor


def main():
    limit = int(5e4)
    sqr = [i ** 2 for i in range(floor(sqrt(limit)) + 1)]   # 所有數字的平方
    result = [(-1,)] * (limit + 1)                          # 建表，將 5e4 以內的答案都列舉出來
    for i in range(floor(sqrt(limit)) + 1):
        for j in range(i, floor(sqrt(limit)) + 1):
            for k in range(j, floor(sqrt(limit)) + 1):
                ans = sqr[i] + sqr[j] + sqr[k]
                if ans <= limit and result[ans] == (-1,):
                    result[ans] = (i, j, k)
    for _ in range(int(input())):
        print(' '.join(map(str, result[int(input())])))


if __name__ == '__main__':
    main()


# def test():
#     import io
#     import sys
#     from contextlib import redirect_stdout
#     import time

#     q = open(r'./test_case/d188_00.in').read()
#     sys.stdin = io.StringIO(q)
#     out_capture = io.StringIO()
#     s = time.time()
#     with redirect_stdout(out_capture):
#         main()
#     print(time.time() - s)
#     q = q.splitlines()
#     ans = iter(open(r'./test_case/d188_00.out').read().splitlines())
#     i = 1
#     for line in out_capture.getvalue().splitlines():
#         a = next(ans)
#         if line != a:
#             print(f'{i}:\n{q[i - 1]}\n{a}\n{line}', end='\n---\n\n')
#         i += 1
#     print('done')


# if __name__ == '__main__':
#     test()
