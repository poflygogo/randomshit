def loveFromMin(n):
    return int(n * (n + 1) / 2)

def loveFromShu(n):
    return int(loveFromMin(n) * (n + 1) - n * (n + 1) * (2 * n + 1) / 6)

while True:
    try:day = int(input())
    except EOFError:break
    print(loveFromMin(day),loveFromShu(day))
