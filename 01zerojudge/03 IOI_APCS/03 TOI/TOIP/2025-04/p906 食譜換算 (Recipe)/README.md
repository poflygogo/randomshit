#

## 解題紀錄

### 1-1 NA(score: 40%)

- 隨意寫的初版

### 1-2 NA(score: 60%)

- 預處理數值計算的部分

```diff
@@ -11 1, +11 2 @@
- print(' '.join(str(ceil(i / a * b)) for i in arr))
+ mul = b // a
+ print(' '.join(str(ceil(i * mul)) for i in arr))
```

huh? 剛好反過來???

### v1-3 NA(score: 90%)

- 修正計算的邏輯，僅保證 40% 的測資中 a 能整除 b

```diff
@@ -11 1, +11, 1 @@
- mul = b // a
+ mul = b / a
```

看來得面對浮點數誤差了

### v1-4 AC(0.1s, 5.8MB)

- 直接使用 Fraction

### v2-1 AC(30ms, 4.8MB)

- 囉嗦起來，寫一個函數處理，徹底擺脫浮點數
