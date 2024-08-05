# 輾轉相除法
a, b = map(int,input().split())

while True:
    if a > b:
        a %= b
    else:
        b %= a
    if a == 0:
        print(b)
        break
    elif b == 0:
        print(a)
        break
