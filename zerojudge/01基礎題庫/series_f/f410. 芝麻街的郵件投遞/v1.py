_ = input()
data = list(map(int, input().split()))
print(
    *[i for i in data if i % 2 == 0],
    *list(reversed([i for i in data if i % 2 == 1]))
)