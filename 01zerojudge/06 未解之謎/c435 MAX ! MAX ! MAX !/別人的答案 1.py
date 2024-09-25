"""
AC(0.1s, 15.6MB)
O(n)

https://zerojudge.tw/ShowThread?postid=30959&reply=0
"""

length = int(input())
data = list(map(int,input().split()))
max_num = 0
max_diff = 0
for i in range(length):
    if data[i] > max_num:
        max_num = data[i]
       
    else:
        max_diff = max(max_diff, max_num - data[i])
print(max_diff)
