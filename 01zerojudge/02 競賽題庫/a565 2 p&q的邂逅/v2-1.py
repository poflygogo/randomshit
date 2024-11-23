# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a565. 2.p&q的邂逅
# 101學年度台北市資訊學科能力競賽


for _ in range(int(input())):
    string = input().replace('.', '').lstrip('q').rstrip('p')
    init = len(string)

    while 'pq' in string:
        string = string.replace('pq', '')
    
    print((init - len(string)) // 2)
