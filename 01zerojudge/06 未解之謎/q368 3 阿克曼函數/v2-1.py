# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q368. 3. 阿克曼函數
# 113學年度新北新莊高中校內資訊學科能力競賽


stack = [tuple(map(int, input().split()))]
cache = {}
while stack:
    m, n = stack.pop()
