from sys import stdin


def three_n_plus_one(num, numbers=None):
    if numbers is None:
        numbers = []
    numbers.append(num)
    if num == 1:
        return len(numbers)
    elif num % 2:
        return three_n_plus_one(3 * num + 1, numbers)
    else:
        return three_n_plus_one(num // 2, numbers)


for line in stdin:
    a, b = sorted(map(int, line.rstrip().split()))
    cycle_length = [three_n_plus_one(i) for i in range(a, b + 1)]
    print(line.rstrip(), max(cycle_length))
