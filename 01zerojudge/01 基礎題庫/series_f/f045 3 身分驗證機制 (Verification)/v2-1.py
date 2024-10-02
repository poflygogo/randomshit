idnum = input()
idnum_digit = sorted(idnum)
print(
    'Good Morning!' if int(idnum[-3:]) == int(idnum_digit[-1]) ** 2 + int(idnum_digit[-2]) ** 2
    else 'SPY!'
)
