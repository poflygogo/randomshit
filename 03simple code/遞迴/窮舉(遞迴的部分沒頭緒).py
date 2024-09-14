"""
據說一切演算法的基礎就是窮舉(所以還是得面對它)

題目:
有 𝑛 支木棒，第 𝑖 支木棒的長度為 𝑎𝑖。我們想從這些棒子中挑出三支，組成三角形。 求總共有幾種挑法。

輸入說明:
輸入有兩行，第一行有一個數字 n，下一行有 n 個數字代表 a1, a2, a3...an。
n <= 100, ai <= 10000

輸出說明:
輸出共有幾種挑法

範例輸入:
4
2 3 4 5

範例輸出:
3

相關連結: [b557. 直角三角形 | ZeroJudge](https://zerojudge.tw/ShowProblem?problemid=b557)
"""


def triangles1(length: int, data: list) -> tuple:
    """
    三層 for 循環
    :param length: 資料長度
    :param data: 資料本體
    :return: (組合總數, 所有的組合)
    """
    cases = set()
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                check: list[int] = [data[i], data[j], data[k]]
                # 三角形定義: 兩條較短的邊長和必定大於最長的邊
                if check[0] + check[1] > check[2]:
                    cases.add(tuple(check))
    cases = tuple(cases)
    return len(cases), cases


def triangles2(length: int, data: list[int]) -> int:
    """遞迴"""
    pass


if __name__ == '__main__':
    a: str = '6'
    b: str = '3 3 4 4 5 5'

    a: int = int(a)
    b: list[int] = [int(i) for i in b.split()]

    ans, case = triangles1(a, b)
    print(
        f'共有 {ans} 種組合, 分別為:',
        *case,
        sep='\n'
    )