from sys import stdin, stdout

def factorize(n):
    factor_data = set()
    for item in range(1, int(n ** 0.5) + 1):
        if n % item == 0:
            factor_data.update({item, n // item})
    factor_data.remove(n)
    return sorted(list(factor_data))

num_init = int(stdin.readline().strip())
factors_init =  factorize(num_init)
factors_init_sum = sum(factors_init)

stdout.write(f'{"+".join(map(str, factors_init))}={factors_init_sum}\n')

if factors_init_sum == num_init:
    stdout.write(f'{num_init} is perfect.\n')

else:
    factors_fri = factorize(factors_init_sum)
    factors_fri_sum = sum(factors_fri)

    stdout.write(f'{"+".join(map(str, factors_fri))}={factors_fri_sum}\n')

    if factors_fri_sum == num_init:
        stdout.write(f'{num_init} and {factors_init_sum} are friends.\n')
    
    else:
        stdout.write(f'{num_init} has no friends.')