hr, mi, sec = map(int, input().split())

if sec >= 60:
    mi += sec // 60
    sec %= 60
if mi >= 60:
    hr += mi // 60
    mi %= 60
if hr >= 24:
    hr %= 24

if sec // 10:
    sec = str(sec)
else:
    sec = f'0{sec}'
if mi // 10:
    mi = str(mi)
else:
    mi = f'0{mi}'
if hr == 0:
    hr = '00'
elif hr // 10:
    hr = str(hr)
else:
    hr = f'0{hr}'

print(hr, mi, sec, sep=':')