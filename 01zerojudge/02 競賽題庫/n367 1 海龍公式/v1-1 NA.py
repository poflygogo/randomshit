from math import sqrt


a, b, c = map(int, input().split())
s = sum((a, b, c)) / 2          # s = x + y + z
x, y, z = s - b, s - c, s - a

if x < 0 or y < 0 or z < 0:
    print('error')

else:
    print(
        f'{x: .4f}\n{y: .4f}\n{z: .4f}',
        f'{sqrt(x * y + y * z + x * z) / 2: .4f}',
        sep='\n'
    )
