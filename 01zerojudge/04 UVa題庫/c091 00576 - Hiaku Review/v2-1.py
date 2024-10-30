from sys import stdin


for line in stdin:
    line = line.rstrip().split('/')
    if line == ['e', 'o', 'i']:
        exit()

    for idx, sentence in enumerate(line):
        cnt = 0
        flag = True
        for i in range(len(sentence)):
            if flag and sentence[i] in 'aeiouy':
                cnt += 1
                flag = False
            elif sentence[i] not in 'aeiou':
                flag = True
        if cnt != (5, 7)[idx % 2]:
            print(idx + 1)
            break
    else:
        print('Y')
