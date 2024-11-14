a, b = map(int, input().split())
print(sum(str(i).count('2') for i in range(a, b + 1)))
