from sys import stdin


def main(n: str, b1: int, b2: int) -> None:
    numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = int(n, base=int(b1))
    b2 = int(b2)

    result = []
    while n > 0:
        result.append(numbers[n % b2])
        n //= b2
    
    print(*reversed(result), sep='')


if __name__ == '__main__':
    for line in stdin:
        num, base1, base2 = line.rstrip().split()
        main(num, int(base1), int(base2))
