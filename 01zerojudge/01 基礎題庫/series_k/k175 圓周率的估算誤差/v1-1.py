import math


n = int(input())
print(
    f'{math.pi - n * math.sin(math.pi / n):.2e}'
)

