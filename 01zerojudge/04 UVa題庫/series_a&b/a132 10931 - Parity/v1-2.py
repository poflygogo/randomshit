n = int(input())
while n:
    bin_n = bin(n)[2:]
    print(f'The parity of {bin_n} is {bin_n.count("1")} (mod 2).')
    n = int(input())
