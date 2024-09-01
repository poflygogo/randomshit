import math

for _ in range(int(input())):
    num = int(input())
    print(
        sum(
            [1 for i in range(2, num + 1) if math.log(i, 2).is_integer() or math.log(i, 5).is_integer()]
        )
    )