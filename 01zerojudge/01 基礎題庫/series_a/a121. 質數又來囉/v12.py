def check_prime(num:int) -> bool:
    """檢查傳入值是否為質數"""
    if num == 1:
        return False
    elif num % 2 == 0 and num != 2:
        return False
    elif num % 3 == 0 and num != 3:
        return False
    else:
        for i in range(5, int(num ** 0.5) + 1, 6):
            if num % i == 0:
                return False
            elif num % (i + 2) == 0:
                return False
    return True

# main
while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break

    result = 0
    for num in range(a, b + 1):
        if check_prime(num):
            result += 1
    
    print(result)
