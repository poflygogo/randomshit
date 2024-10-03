stage, health = map(int, input().split())
die = [int(i) for i in input().split()]
reward = [int(i) for i in input().split()]

for i in range(stage):
    health -= die[i]
    if health < 0:
        break
    health += reward[i]
print(i + 1)
