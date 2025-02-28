MAXW = 50
MAXH = 20

skyline = [[' ' for _ in range(MAXW + 1)] for _ in range(MAXH + 17)]
heightList = [0] * (MAXW + 1)

def initialize():
    for k in range(MAXH + 1):
        for j in range(MAXW + 1):
            heightList[j] = 0
            skyline[k][j] = ' '
        skyline[k][MAXW] = '\0'

def main():
    while True:
        try:
            n = int(input())
            initialize()
            maxHeight = 0

            for _ in range(n):
                startX, width, height = map(int, input().split())

                if height == 0:
                    continue

                if height + 1 > maxHeight:
                    maxHeight = height + 1

                for x in range(startX, min(MAXW, width + startX + 1) + 1):
                    if heightList[x - 1] < height + 1:
                        heightList[x - 1] = height + 1

            for x in range(MAXW):
                skyline[heightList[x]][x] = '-'

            for x in range(MAXW):
                if heightList[x] < heightList[x + 1]:
                    for y in range(heightList[x] + 1, heightList[x + 1]):
                        skyline[y][x + 1] = '|'
                    skyline[heightList[x]][x + 1] = '+'
                    skyline[heightList[x + 1]][x + 1] = '+'
                elif heightList[x] > heightList[x + 1]:
                    for y in range(heightList[x] - 1, heightList[x + 1], -1):
                        skyline[y][x] = '|'
                    skyline[heightList[x]][x] = '+'
                    skyline[heightList[x + 1]][x] = '+'

            if heightList[0] > 0:
                for y in range(1, heightList[0]):
                    skyline[y][0] = '|'
                skyline[0][0] = '+'
                skyline[heightList[0]][0] = '+'

            for y in range(maxHeight, -1, -1):
                print(''.join(skyline[y][:MAXW]))
            print(''.join(str(k % 10) for k in range(1, 51)))
            print()

        except EOFError:
            break

if __name__ == "__main__":
    main()