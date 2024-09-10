for _ in range(int(input())):
    width, _ = input().split()
    data = [input().split() for _ in range(int(width))]
    reverse = [data[i][::-1] for i in range(len(data) - 1, -1, -1)]
    if data == reverse:
        print('go forward')
    else:
        print('keep defending')