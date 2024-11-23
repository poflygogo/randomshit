# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a565. 2.p&q的邂逅
# 101學年度台北市資訊學科能力競賽


from itertools import groupby


for _ in range(int(input())):
    data = input().replace('.', '').lstrip('q').rstrip('p')
    if not data:
        print('0')
    
    else:
        stack = 0
        count = 0
        for key, value in groupby(data):
            length = len(list(value))
            if key == 'p':
                stack += length
            
            elif stack > length:
                stack -= length
                count += length
            
            else:
                count += stack
                stack = 0
        print(count)
