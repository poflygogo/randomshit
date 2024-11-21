# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge b898. 1. 畢氏定理
# 2016高雄市資訊學科能力複賽


arr = [max(input().split(), key=lambda x: (len(x.lstrip('0')), x.lstrip())) for _ in range(int(input()))]
print('\n'.join(arr))
