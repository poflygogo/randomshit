# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11470 Square Sums
# ZeroJudge j062


def main():
    cases = 0
    while True:
        n = int(int(input()))
        if n == 0:
            break
        cases += 1
        matrix = [tuple(map(int, input().split())) for _ in range(n)]
        print(f'Case {cases}: {" ".join(str(i) for i in square_sum(n, matrix))}')


def square_sum(n: int, matrix: list) -> list:
    result = []
    if n % 2 == 0:
        a, b = n // 2 - 1, n // 2
    else:
        a = b = n // 2
    while a >= 0:
        temp = sum(matrix[row][col] for row in sorted({a, b}) for col in range(a, b + 1))
        temp += sum(matrix[row][col] for row in range(a + 1, b) for col in (a, b))
        result.append(temp)
        a -= 1
        b += 1
    result.reverse()
    return result


main()
