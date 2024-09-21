def len_chain() -> list:
    temp = []
    flag, count = data[0], 1
    for i in range(1, len(data)):
        if data[i] == flag:
            count += 1
            continue
        temp.append(count)
        count = 1
        flag = not flag
    else:
        temp.append(count)
    return temp


def get_ans() -> int:
    max_chain, count = 0, 0
    for i in len_chain():
        if i < k:
            max_chain = max(max_chain, count)
            count = 0
        elif i > k:
            count += k
            max_chain = max(max_chain, count)
            count = k
        elif i == k:
            count += k
    return max(max_chain, count)


f = open('test4.txt')
k = int(f.readline())
data = [i.isupper() for i in f.readline().strip()]
print(get_ans())
