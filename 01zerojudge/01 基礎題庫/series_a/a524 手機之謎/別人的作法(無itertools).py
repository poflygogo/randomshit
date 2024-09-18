from sys import stdin


def dfs(pos: int, n: int, ans: list[int], tmp: list[int]):
    """
    :param pos: 指針?
    :param n: n <= 8, 代表學長的密碼位數
    :param ans: 答案存放區, 格式沒看明白
    :param tmp: 取答案時的中間資料
    """
    if pos == n + 1:                    # 檢查指針位置，若超出範圍就輸出 ans
        for i in range(n):
            print(ans[i + 1], end='')
        print()

    for i in range(n, 0, -1):           # 數字由大到小排列
        if tmp[i] == 0:                 # 若對應位置的值為 0 才進行處理(代表沒有用過)
            ans[pos] = i                # 把指針指到的位置設定為 i
            tmp[i] = 1                  # 把已經使用過的數字標記為 1(代表已經用過)
            dfs(pos + 1, n, ans, tmp)   # 呼叫自己，但把指針位置 + 1
            tmp[i] = 0                  # 這步是幹嘛的?


for s in stdin:
    s = s.strip()
    if s:
        dfs(1, int(s), [0] * 10, [0] * 10)

# 遞迴
