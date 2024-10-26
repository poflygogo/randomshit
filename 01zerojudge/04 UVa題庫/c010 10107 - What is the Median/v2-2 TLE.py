from sys import stdin


numbers = [int(stdin.readline().rstrip())]
length = 1
print(numbers[0])
for num in stdin:
    num = int(num.rstrip())
    for i in range(length):
        if numbers[i] >= num:
            numbers.insert(i, num)
            break
    else:
        numbers.append(num)

    length += 1
    if length % 2 == 0:
        a = length // 2
        print(sum(numbers[a - 1: a + 1]) // 2)
    else:
        print(numbers[length // 2])
