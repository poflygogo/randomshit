2020年5月TOI練習賽新手組

## 關鍵字
- 中國剩餘定理
- 離散數學

- [Day 15:[離散數學] 中國餘式定理](https://ithelp.ithome.com.tw/articles/10205772) | [iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/)
## 解題思路

令士兵總數為 n，三種數法的條件分別為
- 每 a1 個人分一組，餘 a2 人
- 每 b1 個人分一組，餘 b2 人
- 每 c1 個人分一組，餘 c2 人

<details>
<summary>用數學關係式表達就是這樣</summary>

```math
\left\{\begin{matrix}
n \equiv (a2 \mod a1) \\
n \equiv (b2 \mod b1) \\
n \equiv (c2 \mod c1) 
\end{matrix}\right.
```
</details>

若

