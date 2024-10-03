def love_from_min(n):
    return int(n * (n + 1) / 2)


def love_from_shu(n):
    return int(love_from_min(n) * (n + 1) - n * (n + 1) * (2 * n + 1) / 6)


while True:
    try:
        day = int(input())
    except EOFError:
        break
    print(love_from_min(day), love_from_shu(day))
