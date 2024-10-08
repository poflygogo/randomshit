data = input()
if data[0] == '-':
    print(-int(data[:0:-1]))
else:
    print(int(data[::-1]))