k, q, r = map(int, input().split())
result = [input()]

# 將字串根據輸入的條件重新排列，並將結果放在同一個 list 中
for _ in range(q):
    result.append(''.join(i[0] for i in sorted(zip(result[-1], input().replace(' ', '')), key=lambda x: x[1])))

# 輸出結果
for i in range(r):
    print(''.join(result[j][i] for j in range(1, q + 1)))
