# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b838. 104北二2.括號問題


def brackets(data) -> int:
    result = 0  # 紀錄成對的括號數量
    cnt = 0     # 紀錄左括號數量
    for i in data:
        if i == '(':
            cnt += 1
        elif cnt > 0:
            cnt -= 1
            result += 1
        else:
            return 0
    if cnt:
        return 0
    else:
        return result


for _ in range(int(input())):
    print(brackets(input().strip()))
