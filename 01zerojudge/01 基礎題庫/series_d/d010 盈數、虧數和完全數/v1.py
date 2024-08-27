from sys import stdin, stdout

def factorize(n:int) -> set:
    factor_data = set()
    for item in range(1, int(n ** 0.5) + 1):
        if n % item == 0:
            factor_data.update({item, n // item})
    factor_data.remove(n)
    return factor_data


for num in stdin:
    num = int(num.strip())
    num_facSum = sum(factorize(num))

    if num == num_facSum:
        stdout.write('完全數\n')
    elif num < num_facSum:
        stdout.write('盈數\n')
    else:
        stdout.write('虧數\n')