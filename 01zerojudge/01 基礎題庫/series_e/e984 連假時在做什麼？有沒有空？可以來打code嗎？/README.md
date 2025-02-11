## 解題思路

原始題目連結: [AtCoder Beginner Contest 161, D-Lunlun Number](https://atcoder.jp/contests/abc161/tasks/abc161_d)

官網解題思路: [PDF](https://img.atcoder.jp/abc161/editorial.pdf)

這邊僅將官網提供的解題思路翻譯成中文。

這個問題可以使用隊列 (Queue) 這種資料結構高效解決。首先，準備一個空的 Queue，並按順序將 1, 2, ..., 9 入隊。然後，進行以下操作 $K$ 次：

- 從 Queue 中取出元素，並將該元素紀錄為 $x$。
- 如果 $x \mod 10 \ne 10$，則將 $10x + (x \mod 10) - 1$ 入隊。
- 將 $10x + (x \mod 10)$ 入隊。
- 如果 $x \mod 10 \ne 9$，則將 $10x + (x \mod 10) + 1$入隊。

在第 $K$ 次操作中取出的數就是第 $K$ 個 Lunlun 數。

> 注意 python 應使用 deque 提高效率，而非 list。
