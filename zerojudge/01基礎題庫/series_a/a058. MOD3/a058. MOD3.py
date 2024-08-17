count_list = [0, 0, 0]
for i in range(int(input())):count_list[int(input()) % 3] += 1
print(*count_list)
