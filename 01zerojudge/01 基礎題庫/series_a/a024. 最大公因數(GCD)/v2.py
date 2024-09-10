def gcd(a :int, b :int) -> int:
    """
    輾轉相除法，求最大公因數
    :param a: 數字1
    :param b: 數字2
    :returns: 數字1和數字2的最大公因數
    """
    while b:
        a, b = b, a % b
    return a

num1, num2 = map(int, input().split())
print(gcd(num1, num2))