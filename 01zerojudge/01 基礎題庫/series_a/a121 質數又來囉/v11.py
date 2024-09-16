# 建立質數表
primes = [2,3,5]
for i in range(7,10001,2):
    flag = True
    for x in primes:
        if x * x > i: break
        if i % x == 0:
            flag = False
            break
    if flag :
        primes.append(i)

# 建好質數表後直接查
while True:
    try:
        a, b = map(int, input().split())
        result = 0
        
        # 所有數字都在質數表內, 直接查就好
        if b <= 10000:
            for prime in primes:
                if prime <= b:
                    if a <= prime:
                        result += 1

                else:
                    break

        # a <= 1e4 <= b, 先處理質數表範圍內的, 再處理範圍外的
        elif a <= 10000:
            for prime in primes[::-1]:
                if prime >= a:
                    result += 1
                else:
                    break
            
            for num in range(10001, b + 1, 2):
                check_num = int(num ** 0.5) + 1
                for prime in primes:
                    if prime <= check_num:
                        if num % prime == 0:
                            result += 1
                    else:
                        break

        # a 和 b 都大於 1e4, 從 a 開始處理, 到 b 結束
        else:
            a += a % 2
            for num in range(a, b + 1, 2):
                check_num = int(num ** 0.5) + 1
                for prime in primes:
                    if prime <= check_num:
                        if num % prime == 0:
                            result += 1
                    else:
                        break

        print(result)
    except EOFError:
        break
