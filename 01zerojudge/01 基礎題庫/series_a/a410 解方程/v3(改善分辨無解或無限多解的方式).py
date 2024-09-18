"""
採用克拉瑪公式Cramer’s Rule解二元一次方程式
有三種狀況，分別為無限多解、無解、單一解
方程式的形式為
ax + by = c
dx + ey = f
"""


def cac_linearEquations(a1, b1, c1, a2, b2, c2):
    """
    解二元一次聯立方程式
    :param args:
        a1, b1, c1: 第一個方程式的係數 interger
        a2, b2, c2: 第二個方程式的係數 interger
    :return: (x, y)，無解或無限多解則返回 False
    """
    _denominator = a1 * b2 - a2 * b1
    if _denominator == 0:
        return False  # 無解或無限多解
    x = (c1 * b2 - c2 * b1) / _denominator
    y = (a1 * c2 - a2 * c1) / _denominator
    return x, y


def cac_parallel(a1, b1, c1, a2, b2, c2):
    """
    判斷無限多解或無解
    :param args:
        a1, b1, c1: 第一個方程式的係數 interger
        a2, b2, c2: 第二個方程式的係數 interger
    :return: 無解="No answer", 無限多解="Too many"
    """
    Dx = c1 * b2 + c2 * b1
    Dy = c1 * a2 + c2 * a1
    if Dx == 0 == Dy:
        return "Too many"
    else:
        return "No answer"


a1, b1, c1, a2, b2, c2 = map(int, input().split())
ans = cac_linearEquations(a1, b1, c1, a2, b2, c2)
if not ans:
    print(cac_parallel(a1, b1, c1, a2, b2, c2))
else:
    print(f"x={ans[0]:.2f}\ny={ans[1]:.2f}")
