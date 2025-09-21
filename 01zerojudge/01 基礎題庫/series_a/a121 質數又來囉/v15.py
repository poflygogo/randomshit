while True:
    try:
        a, b = map(int, input().split())
        cnt = 0

        # 確保 a >= 5
        while a < 5:
            if a in (2, 3) and a <= b:  # 過程要注意超過 b 的值不應計算
                cnt += 1
            a += 1

        # 群找一個 >= a 且符合 6n-1 的數字
        a_mod = a % 6
        if a_mod in (0, 1):
            if a_mod == 0:
                a += 1
            if a > b or a % 2 == 0 or a % 3 == 0:
                pass
            elif all(a % p != 0 and a % (p + 2) != 0 for p in range(5, int(a**0.5) + 1, 6)):
                cnt += 1
            a += 4  # 5 - 1
        else:
            a += 5 - a_mod
        
        for i in range(a, b + 1, 6):
            for num in filter(lambda x: x <= b, (i, i + 2)):
                if num % 2 == 0 or num % 3 == 0:
                    continue
                if all(num % p != 0 and num % (p + 2) != 0 for p in range(5, int(num**0.5) + 1, 6)):
                    cnt += 1
        print(cnt)
    except EOFError:
        break
