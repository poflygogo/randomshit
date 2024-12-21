# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f277. 嘿嘿想不到吧
# sort algorithm, custom sort


data = {}
for _ in range(int(input())):
    name, classroom, id, introduce = input().split()
    data.update({name:{'class':classroom, 'id':id, 'introduce':introduce}})

for name in sorted(data, key=lambda x: (int(data[x]['class']), int(data[x]['id']))):
    print(f"{data[name]['class']} {data[name]['id']} {name}\n{data[name]['introduce']}")
