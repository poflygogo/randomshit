data = list(map(int, input().split()))      # type:list
num = int(input())                          # type:int
count = data.count(num)
total = count * num
print(count, total, sep="\n")
