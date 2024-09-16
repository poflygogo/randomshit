from sys import stdin


for num in stdin:
    num = int(num)
    result = 0
    for i in range(5, num + 1, 5):
        while i % 5 == 0:
            i //= 5
            result += 1
    print(result)
