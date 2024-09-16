from datetime import date

while True:
    try:
        y1, m1, d1 = map(int, input().split())
        y2, m2, d2 = map(int, input().split())
        print(abs(date(y1, m1, d1) - date(y2, m2, d2)).days)
    except EOFError:break
