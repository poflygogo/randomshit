data = []
while True:
    try:
        string = input()
    except EOFError:
        break

    if string in data:
        print("YES")
    else:
        print("NO")
        data.append(string)
