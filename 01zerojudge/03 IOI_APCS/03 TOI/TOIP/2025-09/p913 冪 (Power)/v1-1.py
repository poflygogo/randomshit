# python 3.12
# ZeroJudge p913. 冪 (Power)
# TOI 練習賽 202509 新手組 第2題


n, m = map(int, input().split())
val = n
while val <= m:
    print(val)
    val *= n
