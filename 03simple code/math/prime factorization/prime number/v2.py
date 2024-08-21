"""
只遍歷一半的數字就好
"""

num = int(input())
for i in range(2, num //2 + 1):
    if num % i == 0:
        print("composite number")
        break
else:
    print("prime number")
