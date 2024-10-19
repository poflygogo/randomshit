def luhn_algorithm(num: str) -> bool:
    products = []
    for n, wei in zip(num, [2, 1] * 8):
        product = int(n) * wei
        if product >= 10:
            product = product % 10 + product // 10
        products.append(product)
    
    return not sum(products) % 10


for _ in range(int(input())):
    print('Valid' if luhn_algorithm(input().replace(' ', '')) else 'Invalid')
