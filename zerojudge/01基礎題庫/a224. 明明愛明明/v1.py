while True:
    try:text = input().lower()
    except EOFError:break
    check = [i for i in text if i.isalpha()]
    print('yes !') if check == check[::-1] else print('no...')
