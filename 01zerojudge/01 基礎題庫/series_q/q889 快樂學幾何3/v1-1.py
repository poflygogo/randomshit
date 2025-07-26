# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q889. 快樂學幾何3

# 思路:
# https://mindyourdecisions.com/blog/2024/12/11/challenging-problem-from-turkeys-university-entrance-exam/
# https://www.youtube.com/watch?v=TyZCM76Sx4g

while True:
    try:
        a, b, c, d = map(int, input().split())
        print(c - b + a - d)
    except EOFError:
        break
