def len_chain() -> list:
    """取連續的大寫或小寫數量"""
    temp = []
    flag, count = data[0], 1        # flag 檢查大小寫, count 統計數量
    for i in range(1, len(data)):
        if data[i] == flag:
            count += 1
        else:
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


k = int(input())
data = [i.isupper() for i in input().strip()]   # 不在乎字母，將大小寫用 bool 表示
print(get_ans())
