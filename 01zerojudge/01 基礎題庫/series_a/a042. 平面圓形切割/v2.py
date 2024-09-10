while True:
    try:
        num = int(input())
        print(num ** 2 - num + 2)
    except EOFError:
        break
