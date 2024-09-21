data = [int(i) for i in input().split()] + [None]
count = 0
last_i, curr_i, next_i = 0, 1, 2
while True:
    while data[curr_i] == data[next_i] and data[next_i] is not None:
        next_i += 1
    if data[next_i] is None:
        break
    if data[last_i] < data[curr_i] and data[next_i] < data[curr_i]:
        count += 1
    last_i, curr_i, next_i = curr_i, next_i, next_i + 1
print(count)
