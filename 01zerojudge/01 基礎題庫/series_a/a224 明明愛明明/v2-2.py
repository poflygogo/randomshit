while True:
    try:
        data = tuple(filter(str.isalpha, input().lower()))
    except EOFError:
        break
    alpha = set(data)
    odd = 0
    for i in alpha:
        if data.count(i) % 2 != 0:
            odd += 1
    print('yes !' if odd <= 1 else 'no...')
