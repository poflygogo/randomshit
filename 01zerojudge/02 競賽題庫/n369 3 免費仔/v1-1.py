# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n369. 3. 免費仔
# 112學年度新北新莊高中校內資訊學科能力競賽


data = set()
for _ in range(int(input())):
    mail, name = input().split()
    if mail in data:
        print(f'{name} account has been used')
    else:
        data.add(mail)
        print(f'welcome, {name}')
