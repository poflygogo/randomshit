#

## 解題紀錄

### v1-1 NA(score: 5%) TLE

- 用 `sys.stdin.read(1)` 一個字元一個字元慢慢讀

### v2-1 NA(score: 15%) MLE

- 最樸素的解法，毫無意外得到 MLE

### v3-1 NA(score: 80%) MLE

- 使用 `str.find` 找數字，搭配 `set` 判斷目標數字是否出現過，但是在 `set.add` 時 MLE 了

### v3-2 TLE

- 不建 `set` 了，直接爆搜

### v3-3 TLE

- 借助 split 的 maxsplit 參數切字串

### v3-4 TLE

- 直接用 strip 切字串
