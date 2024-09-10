_ = input()
data = map(lambda x: int(x[::-1]), input().split())
print(max(data))