for _ in range(int(input())):
    num = input()
    num = str(int(num) + int(num[::-1]))
    cnt = 1
    while num != num[::-1]:
        num = str(int(num) + int(num[::-1]))
        cnt += 1
    print(cnt, num)
