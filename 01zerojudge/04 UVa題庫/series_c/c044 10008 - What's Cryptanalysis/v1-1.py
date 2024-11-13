counter = {}                                            # 用來統計字母出現的次數
for _ in range(int(input())):
    for char in input().upper():                        # 先將輸入的字串用 str.upper() 轉換成大寫再遍歷
        if char.isalpha():                              # 只需要判斷是否是字母即可
            counter[char] = counter.get(char, 0) + 1    # dict.get() 可以用來設定預設值

# 把資料 sort 後輸出即可
# 在 sorted() 中傳入 key 可以根據函數回傳值自定義排序方式
for i in sorted(counter, key=lambda x: (-counter[x], x)):
    print(i, counter[i])
