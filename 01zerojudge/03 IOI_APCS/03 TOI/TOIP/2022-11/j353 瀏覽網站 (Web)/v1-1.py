# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j353. 瀏覽網站 (Web)
# 2022-11 TOI 練習賽 新手組


login_info = {}
comm, acc_type = map(int, input().split())
while (comm, acc_type) != (-1, -1):
    if comm == 1:
        login_info[acc_type] = login_info.get(acc_type, 0) + 1
    elif acc_type in login_info:
        login_info.pop(acc_type)
    comm, acc_type = map(int, input().split())
print(sum(login_info.values()))    
