# ZeroJudge b978. 7.最終任務->c.重組提示
# https://zerojudge.tw/ShowProblem?problemid=b978


while True:
    try:
        print("".join(i[0] for i in sorted(zip(input(), map(int, input().split())), key=lambda x: x[1])))
    except EOFError:
        break
