# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e925. pD. 學號檢查
# 2017大學學測推甄申請二階


def is_valid(id: str):
    if not id.startswith('B'):
        return False
    if not id[1:3].isdigit():
        return False
    if not id[3:7] in group:
        return False
    if not id[7:].isdigit():
        return False
    return True

n = int(input())
group = {input() for _ in range(n)}

total_students = 10
failed_counter = 0

for _ in range(total_students):
    if is_valid(input()):
        print('Y')
    else:
        print('N')
        failed_counter += 1

print(f'{failed_counter / total_students:g}')
