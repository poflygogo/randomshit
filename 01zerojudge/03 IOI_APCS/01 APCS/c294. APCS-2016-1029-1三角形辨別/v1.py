a, b, c = sorted(map(int, input().split()))

print(a, b, c)
if (a + b) > c:
    square_a = a ** 2
    square_b = b ** 2
    square_c = c ** 2
    if square_a + square_b < square_c:
        print('Obtuse')
    elif square_a + square_b > square_c:
        print('Acute')
    else:
        print('Right')
else:
    print('No')