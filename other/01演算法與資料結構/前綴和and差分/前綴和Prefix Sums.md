# 前綴和Prefix Sums
前綴和的定義就是各個元素到起點的總和，或者說數列前 n 項的和

是一種重要的*預處理**技巧，能大大降低查詢的時間複雜度

|數字|1|2|3|4|5|6|...|
|-|-|-|-|-|-|-|-|
|前綴和|1|3|6|10|15|21|...|

## 用途
需要頻繁查詢數組中某一區間的元素和的情況

如果沒有先用前綴和預處理，時間複雜度就是 O(n)

但如果用了，可以把時間複雜度壓成 O(1)

例如，在計算機科學中，Prefix Sums 通常用於解決數組中的區間查詢問題，例如求解區間最大子段和、區間平均值、區間中位數等。Prefix Sums還可以用於在數據壓縮、圖像處理和信號處理等領域中，進行離散化、濾波和卷積等操作。

## 使用時機判斷

- **問題是否需要進行區間求和操作**：如果問題需要計算數組中某一區間的元素和，那麼Prefix Sums可能是一個合適的解決方案。
- **數據集的大小**：Prefix Sums通常適用於數據集較小的情況下，因為在預處理階段中需要計算每個元素的前綴和，這可能需要額外的空間和時間。
- **數據是否可以修改**：如果數據集可以修改，那麼在每次修改後，需要重新計算前綴和，這可能會影響算法的效率。因此，在這種情況下，需要仔細考慮使用Prefix Sums的適當性。
- **計算區間求和的頻率**：如果需要頻繁地進行區間求和操作，那麼使用Prefix Sums可能比其他方法更有效。

## Python範例
```py
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prefix_sums = [data[0]]

for idx, item in enumerate(data[1:]):
    prefix_sums.append(prefix_sums[idx] + item)
```

## 其他關鍵字
- 差分
- 區間和
- Bit

## 參考資料
- [Prefix Sums（前綴和）概念](https://claire-chang.com/2023/05/04/prefix-sums%EF%BC%88%E5%89%8D%E7%B6%B4%E5%92%8C%EF%BC%89%E6%A6%82%E5%BF%B5/) | [Claire's Blog](https://claire-chang.com/) 2023-05-04 [2024-08-21]
- [前缀和 & 差分](https://oi-wiki.org/basic/prefix-sum/) | [OI Wiki](https://oi-wiki.org/) 2024-08-21 [2024-08-21]
- [前綴和(prefix sum)](https://hackmd.io/@apcser/ByNGmazhs) | [APCSer](https://hackmd.io/@apcser) | [HackMD](https://hackmd.io/) 2024-05-29 [2024-08-21]
- [Prefix Sum Array - Implementation and Applications in Competitive Programming](https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/) | [GeeksforGeeks](https://www.geeksforgeeks.org/) 2024-01-16 [2024-08-24]
- [Prefix Sums - Problems, Code in C++ & Python](https://www.youtube.com/watch?v=PhgtNY_-CiY) | [Youtube](https://www.youtube.com/) 2023-06-28 [2024-08-21]
- [前綴和與差分](https://cp.wiwiho.me/prefix-sum/) | [WiwiHo 的競程筆記](https://cp.wiwiho.me/) 2024-07-24 [2024-08-21]
- [Prefix sum](https://en.wikipedia.org/wiki/Prefix_sum) | [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) 2024-06-08 [2024-08-21]