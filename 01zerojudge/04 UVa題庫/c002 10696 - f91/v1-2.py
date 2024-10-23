while True:
    num = int(input())
    if not num:
        exit()
    
    print(f'f91({num}) = {91 if num <= 101 else num - 10}')
