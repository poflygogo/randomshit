import time

while True:
    t = time.localtime().tm_sec
    print(t, end='\r')
