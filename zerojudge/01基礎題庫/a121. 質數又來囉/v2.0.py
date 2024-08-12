
# 建立100內的質數表
prime_num = (2, 3, 5, 7, 11, 13, 17, 19, 23,
             29, 31, 37, 41, 43, 47, 53, 59,
             61, 67, 71, 73, 79, 83, 89, 97)

def prime_num_check(num):
  """檢查是否是質數"""
    if num <= 100:
        return CheckLess1e2(num)
    elif num <= 10000:
        return CheckLess1e4(num)
    else:return CheckMore1e4(num)

def CheckLess1e2(num):
  """檢查100內的數字是否在質數表內"""
    for i in prime_num:
        if num == i:
            return True
        elif i > num:
            return False
            break
    else:
        return False

def CheckLess1e4(num):
  """檢查10000內的數字是否能被100內的質數整除"""
    for i in prime_num:
        if num % i == 0:
            return False
    else:
        return True

def CheckMore1e4(num):
  """檢查是否能被6n+1或6n-1的數字整除"""
    if CheckLess1e4(num) == False:
        return False
    else:
        for i in range(101, int(num**0.5)+1, 2):
            if num % i == 0:
                return False
        return True

a, b = map(int,input().split())

count = 0
if a < 5:
    for num in range(a, 4):
        if (num == 2 or num == 3) and num <= b: count += 1
    a = 5

for num in range(5, b+1, 6):
    if prime_num_check(num):count += 1
for num in range(7, b+1, 6):
    if prime_num_check(num):count += 1

print(count)
