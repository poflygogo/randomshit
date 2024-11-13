from sys import stdin


def solve(i, j):
    count = ans = 0
    for cur in range(i, j + 1):
        count = 0
        n = cur
        while True:
            # 如果n之前有計算過，就直接取之前紀錄的值加上去，然後跳出迴圈
            if n in appeared:
                count += appeared[n]
                break

            count += 1
            if n == 1:
                break
            elif n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1

        # 記錄目前數字會進入迴圈幾次
        appeared[cur] = count
        ans = max(count, ans)

    return ans


appeared = {}   # 紀錄出現過的數字
for line in stdin:
    print(line.rstrip(), solve(*sorted(map(int, line.rstrip().split()))))
