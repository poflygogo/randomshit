from sys import stdin


def stream():
    num = ''
    while True:
        char = stdin.read(1)
        if char == ' ':
            yield int(num)
            num = ''
        elif char in ('\n', '\r'):
            yield int(num)
            break
        else:
            num += char


stdin.readline()

result = []
temp_max = next(stream())
temp_min = temp_max
for i in stream():
    i = i
    if i > temp_max:
        result.append(temp_max - temp_min)
        temp_min = temp_max = i
    elif i < temp_min:
        temp_min = i
else:
    result.append(temp_max - temp_min)

print(max(result))
