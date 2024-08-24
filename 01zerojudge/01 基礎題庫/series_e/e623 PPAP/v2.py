ppap = ('Pineapple pen', 'Apple', 'Pineapple', 'Pen')
num = int(input())

n = 1
while (n + 1) * n * 2 < num:
    n += 1

print(ppap[((n + 1) * n * 2 - num) // n])