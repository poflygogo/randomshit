"""
除了3以外，就不需要再檢查諸如 9, 27...等3的倍數了
我們都知道能被2和3整除的數字，必定都是合數
所以6n必定是合數
那6n+1,6n+2...呢?
最後會發現只有 6n+1 和 6n+5 有可能質數
"""

num = int(input())

if num <= 5:
    if num in (2, 3, 5):
        print("prime number")
    else:
        print("composite number")
elif num % 6 != 1 and num % 6 != 5:
    print("composite number")
else:
    check = int(num ** 0.5) + 1
    for i in range(5, check, 6):
        if num % i == 0:
            print("composite number")
            break
    else:
        for j in range(7, check, 6):
            if num % i == 0:
                print("composite number")
                break
        else:
            print("prime number")
