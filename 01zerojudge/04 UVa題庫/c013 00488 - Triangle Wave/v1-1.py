n = int(input())
input()

for _ in range(n):
    amplitude, frequency = int(input()), int(input())
    for _ in range(frequency):
        print(
            *[str(i) * i for i in range(1, amplitude)] + [str(i) * i for i in range(amplitude, 0, -1)],
            sep='\n',
            end='\n\n'
        )
