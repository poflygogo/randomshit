strength = int(input().split()[1])
for i in input().split():
    i = int(i)
    if strength > i:
        strength += i
    else:
        break

print(strength)
