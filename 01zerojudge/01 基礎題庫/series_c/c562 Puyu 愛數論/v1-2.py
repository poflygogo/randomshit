from sys import stdin


for num in stdin:
    num = int(num.strip())
    if num == 0:
        print(1)
    else:
        ans = 0
        while num > 9:
            ans += {
                0: 1, 1: 0, 2: 0, 3: 0, 4: 0,
                5: 0, 6: 1, 7: 0, 8: 2, 9: 1
            }[num % 10]
            num //= 10
        ans += {
            0: 1, 1: 0, 2: 0, 3: 0, 4: 0,
            5: 0, 6: 1, 7: 0, 8: 2, 9: 1
        }[num % 10]
        print(ans)
