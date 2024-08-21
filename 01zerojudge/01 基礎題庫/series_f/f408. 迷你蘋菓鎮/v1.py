length = int(input())
data = list(map(lambda n: (int(n),True) if int(n) > 0 else (int(n),False), input().split()))
data.sort(key= lambda n: abs(n[0]))

result = 0
for index in range(length-1):
    if data[index][1] != data[index+1][1]:
        result += 1

print(result)