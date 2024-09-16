e = eval
while True:
    try:
        print(e(input().replace('/', '//')))
    except EOFError:
        break