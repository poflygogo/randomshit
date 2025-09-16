# ZeroJudge b975. 4.任務三->使眼色遊戲
# https://zerojudge.tw/ShowProblem?problemid=b975

n, m, q = map(int, input().split())

# 紀錄遊戲過程
result = [float("inf")] * (n + 1)
alive = n
round = 1
for _ in range(m):
    k, *player = map(int, input().split())
    if k == alive or len(player) > 1:
        for i in player:
            result[i] = round
        round += 1
        alive -= len(player)


for _ in range(q):
    problem, target = input().split()
    target = int(target)
    # 第 target 回合存活的人數
    if problem == "a":
        print(sum(i > target for i in result) - 1)
    # 第 target 回合存活的人員清單
    elif problem == "b":
        print(*[i for i in range(1, n + 1) if result[i] > target])
    # 編號 target 的人第幾回合被淘汰
    elif problem == "c":
        print(result[target] if result[target] != float("inf") else -1)

print(result[1:])
