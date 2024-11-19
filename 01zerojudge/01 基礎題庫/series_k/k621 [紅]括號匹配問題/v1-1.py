# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k621


stack = []
flag = True
for item in input().rstrip():
    if item in {'(', '['}:
        stack.append(item)
    
    elif stack and stack[-1] == {')': '(', ']': '['}[item]:
        del stack[-1]
    
    else:
        flag = False

if flag and not stack:
    print('Right')

else:
    print('Wrong')
