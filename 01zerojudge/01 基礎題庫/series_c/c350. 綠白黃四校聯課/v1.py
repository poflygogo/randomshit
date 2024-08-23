p_new, a, b = map(int, input().split())

p_used = 0
while p_new >= a:
    p_new -= a
    p_new += b
    p_used += a

print(p_new + p_used)