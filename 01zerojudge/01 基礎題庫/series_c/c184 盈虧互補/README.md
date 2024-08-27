## 解題思路
當我們在討論一個數字的因數時，我們會這樣說:
- 1 的因數為 (1)
- 6 的因數為 (1, 2, 3, 6)
- 7 的因數為 (1, 7)
- 25 的因數為 (1, 5, 25)
- 36 的因數為 (1, 2, 3, 4, 6, 9, 12, 18, 36)

注意到細節了嗎?如果有重複的因數，我們不會重複寫出來，而是視為同一個
- 1 的因數不是 (1, 1)，而是 (1)
- 25 的因數不是 (1, 5, 5, 25)，而是 (1, 5, 25)

一系列不重複的元素，這不就是集合(set)的特性嗎?

於是我們可以使用集合(set)蒐集所有因數，就不需要透過額外的 `if` 處理重複因數的問題

最後注意集合(set)是無序的，但這題輸出因數時應由小排到大，怎麼處理就自己思考。

```py
# 也許會用到的方法method
my_set = set()      # 建立空集合

my_set.add()        # 添加 1 個元素
my_set.union()      # 合併 2 個集合，返回 1 個新集合
my_set.update()     # 合併 2 個集合，將會修改原本的集合
my_set.remove()     # 移除指定元素，若元素不存在會報錯
my_set.discard()    # 移除指定元素，元素不存在不會報錯
```
最後就可以弄出一份像這樣的函數
```py
def factorize(n):
    factor_data = set()
    for item in range(1, int(n ** 0.5) + 1):
        if n % item == 0:
            factor_data.update({item, n // item})
    factor_data.remove(n)
    return sorted(list(factor_data))
```


## 類題
- [c184. 盈虧互補](https://zerojudge.tw/ShowProblem?problemid=c184) | [zerojudge](https://zerojudge.tw/)
- [d010. 盈數、虧數和完全數](https://zerojudge.tw/ShowProblem?problemid=d010) | [zerojudge](https://zerojudge.tw/)

## 解題紀錄
### v1 AC(33ms, 3.4MB)
一次過，完美

### v2 AC(34ms, 3.4MB)
- 修改取因數的方式
    - 對於明顯可見的因數組合(1, 原本的數)，直接添加進去，可以少循環 1 次
    - 但結果沒有比較快