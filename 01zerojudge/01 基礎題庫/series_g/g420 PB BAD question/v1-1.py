stage, health = map(int, input().split())
die = [int(i) for i in input().split()]
reward = [int(i) for i in input().split()]

curr = 0
while curr < stage:
    health -= die[curr]
    if health < 0:
        break
    health += reward[curr]
    curr += 1
print(curr + 1)
