while True:
    try:
        birthday = sum(int(i) * j for i, j in zip(input().split('/'), (100, 1)))
    except EOFError:
        break
    print(
        '摩羯座' if birthday <= 120
        else '水瓶座' if birthday <= 219
        else '雙魚座' if birthday <= 320
        else '牡羊座' if birthday <= 420
        else '金牛座' if birthday <= 521
        else '雙子座' if birthday <= 621
        else '巨蟹座' if birthday <= 722
        else '獅子座' if birthday <= 821
        else '處女座' if birthday <= 923
        else '天秤座' if birthday <= 1023
        else '天蠍座' if birthday <= 1122
        else '射手座' if birthday <= 1222
        else '摩羯座'
    )
