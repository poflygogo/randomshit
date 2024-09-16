"""
採用移項法解二元一次方程式
(先不考慮公式解)
有三種狀況，分別為無限多解、無解、單一解
方程式的形式為
ax + by = c
dx + ey = f
"""

def cac_ratios(*args):
    """
    計算多個數字間的比例
    :param args: 依序輸入x, y, c的係數 interger
    :return: 各係數的比率 list
    """
    _total = sum(args)
    return [n / _total for n in args]

def cac_y(*args):
    """
    計算二元一次方程式的y值
    :param arga: 依序輸入所有係數 interger
    :return: y值 interger
    """
    return (args[5]/args[3]-args[2]/args[0]) / (args[4]/args[3]-args[1]/args[0])

def cac_x(equation, y=0):
    """
    計算x的值
    :param equation: 依序輸入各項係數(x,y,c)
    :param y: y 的值 interger
    :return: x 的值 interger
    """
    return (equation[2]/equation[0])-y * (equation[1]/equation[0])

a, b, c, d, e, f = map(int, input().split())
if a / b == d / e :
    if cac_ratios(a, b, c) == cac_ratios(d, e, f) :
        print("Too many")
    else:
        print("No answer")
else:
    y = cac_y(a, b, c, d, e, f)
    x = cac_x((a, b, c), y)
    print(f"x={x:.2f}\ny={y:.2f}")
