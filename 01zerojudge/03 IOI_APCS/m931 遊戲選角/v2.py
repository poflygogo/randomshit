def func(data):
    a, b = map(int, data.split())
    return a, b, a**2 + b**2

data = [func(input()) for _ in range(int(input()))]
data.sort(key= lambda x:x[2])
print(*data[-2][:2])