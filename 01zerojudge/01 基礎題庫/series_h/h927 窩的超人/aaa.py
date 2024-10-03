"""
改進其他人的答案
https://zerojudge.tw/ShowThread?postid=40775&reply=0
"""

a, b = input().split()
org = [input()]
insert = input()
for i in insert:
    if i == "0":
        org.append(i)
    else:
        org.insert(0, i)
print(int(''.join(org), 2) % 998244353)
