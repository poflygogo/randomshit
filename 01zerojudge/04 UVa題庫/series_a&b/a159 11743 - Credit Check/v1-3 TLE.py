def luhn_algorithm(num: str) -> bool:
    num = [int(i) for i in num]
    for i in range(0, 16, 2):
        if num[i] > 4:
            num[i] = num[i] * 2 - 9
        else:
            num[i] *= 2
    
    return not sum(num) % 10


for _ in range(int(input())):
    print('Valid' if luhn_algorithm(input().replace(' ', '').rstrip()) else 'Invalid')
