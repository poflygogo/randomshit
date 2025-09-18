# ZeroJudge b980. 3rd CPSC Problem 5－－領紅包
# https://zerojudge.tw/ShowProblem?problemid=b980

while True:
    try:
        n, *money = map(int, input().split()[:-1])
        money.sort(reverse=True)
        print(sum(money[:n]))
    except EOFError:
        break
