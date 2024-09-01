def count_power_2and5(n):
    """
    計算範圍內有多少數可以寫成 2^i*5^j的形式
    """
    count = 0
    while n > 1:
        while n % 2 == 0:
            count += 1
            n //= 2
        while n % 5 == 0:
            count += 1
            n //= 5
    return count

for _ in range(int(input())):
    print(
        count_power_2and5(int(input()))
    )