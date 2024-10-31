while True:
    hour, min = map(int, input().split(':'))
    if hour == min == 0:
        exit()
    
    degree = abs(6 * min - hour * 30 - 0.5 * min)
    print(f'{degree if degree < 180 else 360 - degree:.3f}')
