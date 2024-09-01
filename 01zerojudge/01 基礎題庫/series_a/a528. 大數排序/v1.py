while True:
    try:
        data = [int(input()) for i in range(int(input()))]
        print(
            *sorted(data),
            sep='\n'
        )
    except EOFError:
        break