from  math import ceil

ppap = ('Pen', 'Pineapple', 'Apple', 'Pineapple pen')
num = int(input())

n = 1
while (n + 1) * n * 2 < num:
    n += 1

m = num - 2 * n * (n - 1)
remainder = ceil(m / n) - 1
print(ppap[remainder])