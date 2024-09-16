length = int(input())
data = list(map(int, input().split()))
data.sort(key=abs)

result = sum(1 for index in range(length-1) if (data[index] > 0) ^ (data[index+1] > 0))

print(result)