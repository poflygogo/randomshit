while True:
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 == y1 == y2 == 0:
        exit()
        
    elif (x1, y1) == (x2, y2):
        print('0')
    
    elif x1 == x2 or\
         y1 == y2 or\
         round((y2 - y1) / (x2 - x1), 1) in (1.0, -1.0):
        print('1')
    
    else:
        print('2')
