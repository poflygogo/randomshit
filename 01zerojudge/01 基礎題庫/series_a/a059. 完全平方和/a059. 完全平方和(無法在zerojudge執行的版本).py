square_num = []
check = 0

# zerojudge的python版本較舊，不會這一行，但新版本python沒問題
while (n := check**2) <= 1e3:
    square_num.append(n)
    check += 1
square_num = tuple(square_num)

for t in range(int(input())):
    a = int(input())
    b = int(input())
    count = 0
    for n in square_num:
        if a <= n <= b:
            count += n
        elif n > b:
            break
    print(f"Case {t+1}: {count}")
