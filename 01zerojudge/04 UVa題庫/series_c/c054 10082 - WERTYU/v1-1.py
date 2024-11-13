from sys import stdin


keyboard = r" `1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./ "   # 優雅!!
for line in stdin:
    print(*(keyboard[keyboard.index(i) - 1] for i in line.rstrip()), sep='')
