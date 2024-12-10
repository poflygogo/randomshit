# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12908 The book thief
# ZeroJudge e635


import math


while True:
    num = int(input())
    if num == 0:
        break

    total_pages = math.floor(math.sqrt(8 * num + 1) - 1) // 2 + 1
    lost_page = (total_pages + 1) * total_pages // 2 - num
    print(lost_page, total_pages)
