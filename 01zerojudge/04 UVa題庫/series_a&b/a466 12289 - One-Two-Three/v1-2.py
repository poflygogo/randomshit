from sys import stdin


one = 'one'
stdin.readline()
for word in stdin:
    word = word.rstrip()
    if len(word) > 3:
        print(3)
        continue

    if sum((word[i] == one[i] for i in range(3))) >= 2:
        print(1)
    else:
        print(2)
