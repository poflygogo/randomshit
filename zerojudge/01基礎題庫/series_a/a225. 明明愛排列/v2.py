from sys import stdin

for _ in stdin:
    data = list(map(int, stdin.readline().split()))
    data.sort(key= lambda num: (num%10, -num//10))
    print(*data)
