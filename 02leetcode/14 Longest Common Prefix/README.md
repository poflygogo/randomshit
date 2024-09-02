## 需要的知識
- 理解 sort() 和 sorted() 的原理與使用方式

## 解題紀錄
### v1.0
- Runtime: 16ms | Beats 60.81%
- Memory: 11.75MB | Beats 88.59%
- 時間複雜度: O(n^2)

### v1.1
- Runtime: 19ms | Beats 39.22%
- Memory: 11.81MB | Beats 62.17%
- 時間複雜度: O(n^2)
> 原本以為是降低效率的東西，竟然能提高效率? 看來我需要對 `sort()` 預設的行為更進一步的認識 

## 別人的答案
```python
def longestCommonPrefix(strs):
    ans = ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if (first[i] != last[i]):
            return ans
        ans += first[i]
    return ans 
```
- Runtime: 12ms | Beats 84.89%
- Memory: 12.02MB | Beats 5.27%
- 時間複雜度: O(n)

直接利用 sort 針對字串進行排序，可預知第一個字串與最後一個字串是"最不相同的"，所以只需要比較第一個和最後一個字串即可，這樣就不需要遍歷整個 list 了
