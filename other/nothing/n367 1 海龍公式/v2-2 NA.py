from decimal import Decimal


def is_not_triangle(n1: int, n2: int, n3: int) -> bool:
    """
    判斷三角形條件是否成立
    n1, n2, n3 分別為三個邊的平方
    若不成立則返回 True
    """
    _temp = sorted((n1, n2, n3))
    if sum(map(lambda x: Decimal(x).sqrt(), _temp[:2])) > Decimal(_temp[2]).sqrt():
        return False
    return True
    


a, b, c = map(int, input().split())
if is_not_triangle(a, b, c):
    print('error')

else:
    s = sum((a, b, c)) / 2
    x, y, z = s - b, s - c, s - a
    print(
    f'{x: .4f}\n{y: .4f}\n{z: .4f}',
    f'{Decimal(x * y + y * z + x * z).sqrt() / 2: .4f}',
    sep='\n'
    )
