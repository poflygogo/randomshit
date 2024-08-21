# 1000000000 <= num <= 999999999
# 1e9 <= num <= 1e10-1

def check_goodguy(num:int) -> bool:
    if num < 200000000:
        return True
    else:
        for i in range(2, 10):
            if num % i == 0 and 100000000 <= num // i < 200000000:
                return False
        else:
            return True


num = int(input())
if check_goodguy(num):
    print('yes')
else:
    print('no')