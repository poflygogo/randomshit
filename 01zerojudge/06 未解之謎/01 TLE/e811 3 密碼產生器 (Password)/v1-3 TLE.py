# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e811. 3. 密碼產生器 (Password)
# 2019-11 TOI 練習賽 潛力組


def password_generator(P, Q, R, a0, a1, N):
    for _ in range(N - 1):
        a0, a1 = a1, (P * a1 + Q * a0 + R) % 10000
    return str(a1).zfill(4)


def main():
    print(password_generator(*map(int, input().split())))


if __name__ == '__main__':
    main()
