def luhn_algorithm(num: str) -> bool:
    num = [int(i) for i in num]
    for i in range(0, 16, 2):
        num[i] *= 2
        if num[i] > 9:
            num[i] = num[i] % 10 + 1
    
    return not sum(num) % 10


for _ in range(int(input())):
    print('Valid' if luhn_algorithm(input().replace(' ', '').rstrip()) else 'Invalid')
