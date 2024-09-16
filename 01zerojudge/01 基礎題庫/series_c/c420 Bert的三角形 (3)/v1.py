num = int(input())
length = (num - 1) * 2 + 1

for i in range(num):
    space = '_' * (length // 2 - i)
    print(f"{space}{'*' * (i * 2 + 1)}{space}")