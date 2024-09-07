from sys import stdin

def get_time(n:int) -> list:
    data = []
    for _ in range(n):
        a, b = map(int, next(stdin).split())
        if data and data[-1][1] == a:
            data[-1][1] = b
        else:
            data.append([a, b])
    return data

def meeting(l1:list, l2:list, time:int) -> tuple:
    if not l1 or not l2: return -1,
    for a1, a2 in l1:
        for b1, b2 in l2:
            if b1 >= a2: break
            if b2 <= a1: continue
            if b1 <= a1 and a1 + time <= b2:
                return a1, a1 + time
            if a1 < b1 and b1 + time <= a2:
                return b1, b1 + time
    return -1,

n, m = map(int, next(stdin).split())
ming = get_time(n)
awen = get_time(m)
d = int(next(stdin))

ming = [i for i in ming if i[1] - i[0] >= d]
awen = [i for i in awen if i[1] - i[0] >= d]

print(*meeting(ming, awen, d))