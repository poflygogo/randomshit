a, b, c = sorted(map(int, input().split()))

square_a = a ** 2
square_b = b ** 2
square_c = c ** 2

if square_a + square_b < square_c: print('obtuse triangle')
elif square_a + square_b > square_c: print('acute triangle')
else: print('right triangle')
