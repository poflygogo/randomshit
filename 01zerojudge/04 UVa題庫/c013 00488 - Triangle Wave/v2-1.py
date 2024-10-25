n = int(input())
input()

for _ in range(n):
    amplitude, frequency = int(input()), int(input())
    result = '\n'.join([str(i) * i for i in range(1, amplitude)] + [str(i) * i for i in range(amplitude, 0, -1)]) + '\n'
    for _ in range(frequency):
        print(result)
