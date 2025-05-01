# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b923. stack 堆疊的模板題


stack = []
for _ in range(int(input())):
    comm = input().split()
    if comm[0] == '1':
        stack.pop()
    elif comm[0] == '2':
        print(stack[-1])
    elif comm[0] == '3':
        stack.append(comm[1])
