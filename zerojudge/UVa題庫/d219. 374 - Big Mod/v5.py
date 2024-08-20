while True:
    P = int(input().strip())
    B = int(input().strip())
    M = int(input().strip())

    print(pow(B, P, M))

    try:
        _ = input()
    except EOFError:
        break