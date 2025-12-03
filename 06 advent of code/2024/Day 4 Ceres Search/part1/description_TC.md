# --- 第四天：穀神星搜索 (Ceres Search) ---

「看來首席不在這裡。下一個！」其中一位歷史學家拿出一個裝置並按下上面唯一的按鈕。在一陣短暫的閃光後，你認出了這是 [穀神星監測站](https://adventofcode.com/2019/day/10) 的內部！

隨著尋找首席的行動繼續進行，一位住在站裡的小精靈拉了拉你的襯衫；她想知道你能不能幫她解她的單字搜尋謎題（你的拼圖輸入）。她只需要找到一個字：`XMAS`。

這個單字搜尋允許單字是水平的、垂直的、對角的、倒著寫的，甚至是與其他單字重疊的。不過這有點不尋常，因為你不僅僅是要找到一個 `XMAS` —— 你需要找到所有的 `XMAS`。以下是 `XMAS` 可能出現的幾種方式，其中無關的字元已被替換為 `.`：

```text
..X...
.SAMX.
.A..A.
XMAS.S
.X....
```

實際的單字搜尋將會充滿字母。例如：

```text
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```

在這個單字搜尋中，`XMAS` 總共出現了 `18` 次；這裡是同一個單字搜尋，但未參與任何 `XMAS` 的字母已被替換為 `.`：

```text
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
```

看看小精靈的單字搜尋。`XMAS` 出現了多少次？
