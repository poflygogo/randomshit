width = int(input())
direct = int(input())
arr = ''.join([input().strip().replace(' ', '') for _ in range(width)])
offset = (-1, -width, 1, width)
pos = width ** 2 // 2
print(arr[pos], end='')
for i in range(1, width):
    for _ in range(2):
        for _ in range(i):
            pos += offset[direct]
            print(arr[pos], end='')
        direct = (direct + 1) % 4
for _ in range(i):
    pos += offset[direct]
    print(arr[pos], end='')
print()
