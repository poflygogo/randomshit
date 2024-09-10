import time


t = time.localtime().tm_sec % 5
if t == 1:
    print('Hello, World!')
    time.sleep(1)
elif t == 2:
    print('hello, world')
    time.sleep(1)
elif t == 3:
    print('Halo, word!!!')
    time.sleep(0.75)
elif t == 4:
    print('世界，您好！')
    time.sleep(0.75)
else:
    print('https://zerojudge.tw/ShowProblem?problemid=a001')