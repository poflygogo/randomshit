"""
偶數必定是合數
若自然數 n 沒有小於或等於根號 n 的質因數，則 n 就是質數
"""

num = int(input())
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print("composite number")
        break
else:
    print("prime number")
