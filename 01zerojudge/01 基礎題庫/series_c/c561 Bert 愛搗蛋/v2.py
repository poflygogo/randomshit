_ = input()
print(
    max(input().split(),key= lambda x: (len(x), int(x[::-1])))[::-1]
)