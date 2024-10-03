stage, health = map(int, input().split())
die = input().split()
reward = input().split()

curr = 0
while curr < stage:
    health -= int(die[curr])
    if health < 0:
        break
    health += int(reward[curr])
    curr += 1
print(curr + 1)
