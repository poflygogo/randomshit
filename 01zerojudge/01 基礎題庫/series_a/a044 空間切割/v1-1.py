# 公式解
while True:
    try:
        n = int(input())
        print((n ** 3 + 5 * n + 6)//6)
    except EOFError:
        break
