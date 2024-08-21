while True:
    print(input())
    mark = input()
    print(
        *(input().split(mark)),
        sep='\n'
    )
    try:
        input()
    except EOFError:
        break