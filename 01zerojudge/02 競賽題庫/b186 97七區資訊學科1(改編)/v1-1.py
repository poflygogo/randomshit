while True:
    try:
        cookie, chocolate, cake = map(int, input().split())
    except EOFError:
        exit()
    else:
        print(f'{cookie} 個餅乾，{chocolate + min(cookie // 10, cake // 2)} 盒巧克力，{cake} 個蛋糕。')
