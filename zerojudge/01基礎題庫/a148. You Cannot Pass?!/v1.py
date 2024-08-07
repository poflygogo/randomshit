while True:
    try: numlist = list(map(int,input().split()))
    except EOFError: break
    length = numlist.pop(0)
    if sum(numlist)/length > 59:print('no')
    else:print('yes')
