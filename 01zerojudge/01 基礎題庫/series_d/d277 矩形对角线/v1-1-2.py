while True:
    try:
        print(int(input()) // 2 * 2)
    except EOFError:
        break
