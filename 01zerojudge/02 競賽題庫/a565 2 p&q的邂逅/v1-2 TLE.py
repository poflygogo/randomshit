# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a565. 2.p&q的邂逅
# 101學年度台北市資訊學科能力競賽


for _ in range(int(input())):
    stack = 0
    count = 0
    for i in input().replace('.', '').lstrip('q').rstrip('p'):
        if i == 'p':
            stack += 1
        
        elif stack > 0:
            stack -= 1
            count += 1
    
    print(count)