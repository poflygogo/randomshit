# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e940. pA. 猜單字遊戲
# 2009大學學測推甄申請二階


target = input().rstrip()
target_flag = {i:False for i in target}

print('*' * len(target))
for _ in range(int(input())):
    target_flag[input()] = True
    print(''.join(("*", i)[target_flag[i]] for i in target))
