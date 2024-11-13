data = []
while True:
    num = int(input().rstrip())
    if not num:
        break
    data.append(num)
print(sum(data))
