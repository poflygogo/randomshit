for _ in range(int(input())):
    width, _ = input().split()
    data = [input().split() for _ in range(int(width))]
    reverse = [i[::-1] for i in data[::-1]]
    if data == reverse:
        print('go forward')
    else:
        print('keep defending')