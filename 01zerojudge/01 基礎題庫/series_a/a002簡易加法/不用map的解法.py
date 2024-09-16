# 方法1
a = input() # 2 3
a = a.split(' ') # ['2', '3']
a = int(a[0])+int(a[1])
print(a)

# 方法2
(lambda x, y: print(int(x) + int(y)))(*input().split())
