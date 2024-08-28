while True:
    num = bin(int(input()))
    if num == '0b0':
        break

    print(len(num) - len(num.rstrip("1")))