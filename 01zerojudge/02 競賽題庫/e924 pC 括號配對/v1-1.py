# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e924. pC. 括號配對
# 2017大學學測推甄申請二階


def is_valid(s: str):
    if len(s) % 2:
        return False
    
    bracket = {")": "(", "]": "[", ">": "<", "}": "{"} 
    stack = []
    for i in s:
        if i in bracket:
            if stack and stack[-1] == bracket[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)

    if stack:
        return False
    else:
        return True


for _ in range(int(input())):
    if is_valid(input().rstrip()):
        print("Y")
    else:
        print("N")
