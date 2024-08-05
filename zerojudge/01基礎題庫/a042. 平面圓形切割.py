while True:
    try:
        num = 2
        for i in range(1, int(input())+1):
            num += ( i - 1 ) * 2
        print(num)
    except:break
