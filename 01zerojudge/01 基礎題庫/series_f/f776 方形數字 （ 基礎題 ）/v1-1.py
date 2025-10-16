def calc(x: int, y: int) -> int:
    if x > y:
        x, y = y, x
    h = (2 * x * (x + 1) * (2 * x + 1) // 6) - (x * (x + 1) // 2)
    k = (x + 1 + y) * (y - x) // 2 * x
    return h + k


def main():
    input()  # for what?
    for _ in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        print(calc(x2, y2) - calc(x2, y1 - 1) - calc(x1 - 1, y2) + calc(x1 - 1, y1 - 1))


main()
