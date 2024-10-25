n = int(input())
input()

for _ in range(n):
    amplitude, frequency = int(input()), int(input())
    for _ in range(frequency):
        for i in range(1, amplitude):
            print(str(i) * i)
        for i in range(amplitude, 0, -1):
            print(str(i) * i)
        print()
