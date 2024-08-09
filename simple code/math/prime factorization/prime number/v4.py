"""
有些數字不需要重複判斷
例如2的倍數一定是偶數，早就在一開始便得知了
如果不能被2整除，則必定不會被4, 6, 8,...,2n的數字整除
除果有因數，除了2以外，必定是奇數
"""
num = int(input())

if num == 2:
    print("prime number")
else:
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            print("composite number")
            break
    else:
        print("prime number")
