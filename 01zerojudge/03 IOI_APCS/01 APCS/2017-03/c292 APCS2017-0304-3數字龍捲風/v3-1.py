def tornado(w: int):
    for i in range(1, w):
        yield i
        yield i
    yield i


width = int(input())
direct = int(input())
array = ''.join([input().strip().replace(' ', '') for _ in range(width)])
offset = (-1, -width, 1, width)

pos = width ** 2 // 2
result = array[pos]
for i in tornado(width):
    for _ in range(i):
        pos += offset[direct]
        result += array[pos]
    direct = (direct + 1) % 4
print(result)
