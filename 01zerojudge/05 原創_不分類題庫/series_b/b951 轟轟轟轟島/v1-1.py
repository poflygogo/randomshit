# ZeroJudge b951. 轟轟轟轟島
# https://zerojudge.tw/ShowProblem?problemid=b951
# 105學年度復旦程式設計班檢定考

# Greedy
# 在邊長總長度為固定值的情況下，長寬比越接近 1:1 面積就會越大

from typing import List

def max_size(sticks: List[int]) -> int:
    sticks.sort(reverse=True)
    a = b = 0
    for i in sticks:
        if a >= b:
            b += i
        else:
            a += i
    return a * b

def main():
    while True:
        try:
            print(max_size(list(map(int, input().split()))))
        except EOFError:
            break

main()
