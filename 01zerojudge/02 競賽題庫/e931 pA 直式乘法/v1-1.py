# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e931. pA. 直式乘法
# 2014大學學測推甄申請二階


a, b = int(input()), int(input())

# 計算所有相關的數字
arr = [str(a), str(b)]
ans = str(a * b)
while b:
    b, t = divmod(b, 10)
    arr.append(str(a * t))
arr.append(ans)

# 計算最大寬度
width = max(len(i) for i in arr)

# 格式化
arr[0] = arr[0].rjust(width)
arr[1] = arr[1].rjust(width)
arr[-1] = arr[-1].rjust(width)
for i in range(2, len(arr) - 1):
    arr[i] = arr[i].rjust(width - (i - 2))

# 插入分隔符號
bar = '-' * width
arr.insert(2, bar)
arr.insert(-1, bar)

print('\n'.join(arr))
