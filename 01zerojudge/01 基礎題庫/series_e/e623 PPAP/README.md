# PPAP
> Apple pen~ Pineapple pen~ uh! Pen-Pineapple-Apple-Pen!

這首《Pen-Pineapple-Apple-Pen》，簡稱《PPAP》，是一首於 2016 年 8 月 25日發表的歌曲，這首歌在一個月內引發了日本高中生的模仿熱潮，亦有藝人跟著拍成短片，甚至成為日本全民運動。

在菜市場工作的小 P 聽到這首歌後為之瘋狂，於是決定在菜市場發放號碼牌，再依照號碼牌上的數字分送出 Pen、Pineapple、Apple、Pineapple pen。每一輪每一種物品的發放數量都是前一輪加一個（四種物品循環算一輪），也就是發放到第 n 輪時每一種都會送出 n 個，舉例說明前 27 個發放的物品如下：

| 1   | Pen(第1輪)      | 2   | Pineapple(1)      | 3   | Apple(1)          | 4    | Pineapple pen(1)  |
|:----|:--------------|:----|:------------------|:----|:------------------|:-----|:------------------|
| 5   | Pen(第2輪)      | 6   | Pen(2)            | 7   | Pineapple(2)      | 8    | Pineapple(2)      |
| 9   | Apple(2)      | 10  | Apple(2)          | 11  | Pineapple pen(2)  | 12   | Pineapple pen(2)  |
| 13  | Pen(第3輪)      | 14  | Pen(3)            | 15  | Pen(3)            | 16   | Pineapple(3)      |
| 17  | Pineapple(3)  | 18  | Pineapple(3)      | 19  | Apple(3)          | 20   | Apple(3)          |
| 21  | Apple(3)      | 22  | Pineapple pen(3)  | 23  | Pineapple pen(3)  | 24   | Pineapple pen(3)  |
| 25  | Pen(第4輪)      | 26  | Pen(4)            | 27  | Pen(4)            | ...  | 依此類推              |

若拿到 17 號的號碼牌，之後便可領到 Pineapple。為了預知自己會拿到的物品，請你寫一支程式判斷當前拿到的號碼牌會得到 Pen、Pineapple、Apple 還是Pineapple pen。

### 輸入格式
輸入一個正整數 $ N(1 \le N \le 10000)$，代表拿到的號碼牌的數字

### 輸出格式
根據拿到的號碼，輸出 Pen, Pineapple, Apple 或 Pineapple Pen。

|    | 輸入   | 輸出    |
|:---|:-----|:------|
| #1 | 87   | Pen   |
| #2 | 4076 | Apple |

## 解題思路
先建立一個陣列，用來保存四種元素<br>
['Pen', 'Pineapple', 'Apple', 'Pineapple pen']

### 推導公式 1, O(n)
把所有可能的條件都列出來的確可行，但這將消耗大量 memory ，建表也是很麻煩的事情，如果資料範圍再改，將導致需要重新建立新表格。

- 第 1 輪的元素位置: 1 to 4 , 元素總數 = 4 = 4 * 1
- 第 2 輪的元素位置: 5 to 12, 元素總數 = 8 = 4 * 2
- 第 3 輪的元素位置: 13 to 24, 元素總數 = 12 = 4 * 3
- 第 n 輪的元素位置: 2n(n - 1) + 1 to 2n(n + 1) 元素總數 = 4n
  - n 是大於 0 的正整數

'Pen' 的位置範圍
- 第 1 輪的 'Pen' 的位置: 1 to 1
- 第 2 輪的 'Pen' 的位置: 5 to 6
- 第 3 輪的 'Pen' 的位置: 13 to 15
- 第 n 輪的 'Pen' 的位置: 2n(n-1)+1 to 2n(n-1)+(n-1)

將輸入的值減去 2n(n-1) 就是第 n 輪的第 m 位置<br>
取 remainder = m / n 並無條件進位取整數
  - remainder = 1 -> 'Pen'
  - remainder = 2 -> 'Pineapple'
  - remainder = 3 -> 'Apple'
  - remainder = 4 -> 'Pineapple pen'

### 推導公式 2

- 進行到第 1 輪的元素總數: 4 = 2 * 1 * 2
- 進行到第 2 輪的元素總數: 12 = 3 * 2 * 2
- 進行到第 3 輪的元素總數: 24 = 4 * 3 * 2
- 進行到第 n 輪的元素總數: n(n+1) * 2

## 解題紀錄
### v1 AC(42ms, 3.3MB)
- 時間複雜度: O(n)

這效率不是很滿意<br>
要怎麼做才能加速找到 n 的速度呢 hmm

### v2 AC(22ms, 3.3MB), (27ms, 3.3MB), (38ms, 3.3MB)
- 時間複雜度: O(n)
- 修改計算方式，現在不用導包也能做了

阿怎麼越測越慢?