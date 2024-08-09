"""
遍歷所有比它小的整數
"""

num = int(input())
for i in range(2, num):
    if num % i == 0:
        print("composite number")
        break
else:
    print("prime number")
