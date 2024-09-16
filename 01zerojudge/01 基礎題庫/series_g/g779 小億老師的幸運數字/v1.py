num1, num2 = input().split()

if (num2 in num1) or (int(num1) % int(num2) == 0):
    print("YES")
else:
    print("NO")