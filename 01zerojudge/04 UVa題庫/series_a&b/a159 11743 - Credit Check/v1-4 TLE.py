def luhn_algorithm(num: str) -> bool:
    num = [int(i) for i in num]
    pre_cac = {
        0: 0, 1: 2, 2: 4, 3: 6, 4: 8,
        5: 1, 6: 3, 7: 5, 8: 7, 9: 9
    }
    
    return not sum([num[i] for i in range(1, 16, 2)] + [pre_cac[num[i]] for i in range(0, 16, 2)]) % 10


for _ in range(int(input())):
    print('Valid' if luhn_algorithm(input().replace(' ', '').rstrip()) else 'Invalid')
