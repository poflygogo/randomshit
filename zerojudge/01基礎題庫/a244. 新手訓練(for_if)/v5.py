"""
sys.stdin和input相似，都是輸入數據的手段
99%情況下使用input即可
但如果需要對數據精細化處理，就可能需要sys.stdin
此外sys.stdin還有個優勢是輸入數據的效率較佳

追求可讀性時使用input()
追求效率時改用sys.stdin
"""

# 導入sys module 的 stdin function
from sys import stdin

# 用法類似讀取文件時的操作
data = stdin.readlines()

# list comprehension 處理數據，並移除第一行(因為所有的資料全進來了，不需要知道有幾組了)
data = [line.strip() for line in data][1:]

# 剩下就是正常操作
for line in data:
    # 用map()會比list comprehension效率高
    a, b, c= map(int, line.split())
    if a == 1:print(b + c)
    elif a == 2:print(b - c)
    elif a == 3:print(b * c)
    else:print(int(b / c))
