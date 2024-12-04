# -*- encoding: utf-8 -*-
# python 3.6
# zerojudge a810. 1. 倍數關係
# 102學年度高雄市資訊學科能力競賽複賽

def lcm(num1, num2):
    def gcd(_num1, _num2):
        return _num1 if _num2 == 0 else gcd(_num2, _num1 % _num2)
    return num1 * num2 // gcd(num1, num2)


a, b, x, y = map(int, input().split())
x, y = map(lambda n: abs(n) if n != 0 else 1, (x, y))
if a >= 0:
    b -= a
    print(b // x + b // y - b // lcm(x, y) + 1)
else:
    a = abs(a)
    print(
        a // x + a // y - a // lcm(x, y) +
        b // x + b // y - b // lcm(x, y) + 
        1
    )