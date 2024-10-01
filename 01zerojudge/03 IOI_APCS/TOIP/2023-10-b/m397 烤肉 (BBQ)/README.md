TOIP 202310-b2 烤肉 (BBQ)

## 解題思路
根據題意，可列出如下關係式:

令阿榮共買了 a 個豬肉串和 b 個牛肉串，則
- M = a + b
- N = Xa + Yb

移項處理後可得 a = M - b，代入第二式

N = X(M - b) + Yb = XM - Xb + Yb = XM + (Y - X)b

b = (N - XM) / (Y - X)

## 解題紀錄
### v1-1 AC(18ms, 3.3MB)
