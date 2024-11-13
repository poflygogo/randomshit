for _ in range(int(input())):
    num = int(input())
    num += int(str(num)[::-1])
    cnt = 1

    while str(num) != str(num)[::-1]:
        num += int(str(num)[::-1])
        cnt += 1

    print(cnt, num)
