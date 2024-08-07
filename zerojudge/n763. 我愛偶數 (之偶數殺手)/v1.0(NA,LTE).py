length = int(input())
num_list = list(map(int, input().split()))

while len(num_list) > 1:
    num = num_list.pop(0)
    if num % 2 == 0:
        num_list.pop(0)
    num_list.append(num)
print(*num_list)
