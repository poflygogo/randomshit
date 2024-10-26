from sys import stdin
from bisect import bisect_left


numbers = [int(stdin.readline().rstrip())]
length = 1
print(numbers[0])
for num in stdin:
    num = int(num.rstrip())

    # 二分搜尋找插入的位置
    numbers.insert(bisect_left(numbers, num), num)

    length += 1
    if length % 2 == 0:
        a = length // 2
        print(sum(numbers[a - 1: a + 1]) // 2)
    else:
        print(numbers[length // 2])
