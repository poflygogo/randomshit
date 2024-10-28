## 解題思路
這題目參考這張圖片:

![image](https://upload.wikimedia.org/wikipedia/commons/8/85/Diagonal_argument.svg)
<br>[wikipedia](https://zh.wikipedia.org/wiki/File:Diagonal_argument.svg)

把圖片翻轉 45 度後，可以得到像這樣的三角形

```text
->         1/1
<-       2/1  1/2
->     3/1  2/2  1/3
<-   4/1  3/2  2/3  1/4
-> 5/1  4/2  3/3  2/4  1/5
```
只需要先判斷目標數字位於第幾層，即可得知應該要由左至右還是由右至左

## 解題紀錄
### v1-1 AC(0.2s, 3.3MB)
### v1-2 AC(0.2s, 3.3MB)
- 調整資料處理方式
> 或許算法還能再改進?