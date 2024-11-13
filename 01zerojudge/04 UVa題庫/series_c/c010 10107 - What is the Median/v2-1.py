from sys import stdin


numbers = []
length = 0
for num in stdin:
    numbers.append(int(num))
    numbers.sort()
    length += 1
    if length % 2 == 0:
        a = length // 2
        print(sum(numbers[a - 1: a + 1]) // 2)
    else:
        print(numbers[length // 2])
