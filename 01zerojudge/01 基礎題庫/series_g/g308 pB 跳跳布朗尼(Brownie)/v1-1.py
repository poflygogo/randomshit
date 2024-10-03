n, t = map(int, input().split())
teleport = [int(i) for i in input().split()]
chocolate = [int(i) for i in input().split()]
visited = [True] * n

eat = 0
while visited[t]:
    eat += chocolate[t]
    visited[t] = False
    t = teleport[t]
print(eat)
