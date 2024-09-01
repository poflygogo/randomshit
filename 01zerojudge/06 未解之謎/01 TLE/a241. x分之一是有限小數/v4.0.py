import math

for _ in range(int(input())):
    num = int(input())
    print(
        math.floor(math.log(num, 2)) + math.floor(math.log(num, 5))
    )