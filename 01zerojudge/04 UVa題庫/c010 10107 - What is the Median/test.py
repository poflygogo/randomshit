from sys import stdin


numbers = []
for num in stdin:
    numbers.append(int(num))
    numbers.sort()
    if len(numbers) % 2 == 0:
        a = len(numbers) // 2
        print(sum(numbers[a - 1: a + 1]) // 2)
    else:
        print(numbers[len(numbers) // 2])
