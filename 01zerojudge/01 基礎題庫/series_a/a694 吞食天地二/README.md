## 類題
keyword 前綴和
- [a694. 吞食天地二](https://zerojudge.tw/ShowProblem?problemid=a694)
- [e339. 前綴和練習](https://zerojudge.tw/ShowProblem?problemid=e339)
- [d563. 等值首尾和](https://zerojudge.tw/ShowProblem?problemid=d563)
- [d206. 00108 - Maximum Sum](https://zerojudge.tw/ShowProblem?problemid=d206)
- [e346. 區間和練習](https://zerojudge.tw/ShowProblem?problemid=e346)
- [e856. 旅行者_九國遊歷記<10> 立方 (Square)](https://zerojudge.tw/ShowProblem?problemid=e856)([抄](https://home.gamer.com.tw/artwork.php?sn=4746642))
- [f174. m6a2-蛋糕(Cake)](https://zerojudge.tw/ShowProblem?problemid=f174)
- [f314. 3. 勇者修煉](https://zerojudge.tw/ShowProblem?problemid=f314)
- [f581. 3. 圓環出口](https://zerojudge.tw/ShowProblem?problemid=f581)
- [f816. TOI_y21m4_a02Youtube](https://zerojudge.tw/ShowProblem?problemid=f816)
- [g597. 3. 生產線](https://zerojudge.tw/ShowProblem?problemid=g597)
- [h065. 一二三木頭人 (Freeze)](https://zerojudge.tw/ShowProblem?problemid=h065)
- [h074. Chinese Restaurant (Harder Version)](https://zerojudge.tw/ShowProblem?problemid=h074)
- [i178. 比大小 (Cards)](https://zerojudge.tw/ShowProblem?problemid=i178)
- [k290. 借款金額 (Loan)](https://zerojudge.tw/ShowProblem?problemid=k290)
- [k572. pC. 關於冷氣調溫這件事](https://zerojudge.tw/ShowProblem?problemid=k572)
- [k707. 老鼠愛前綴和](https://zerojudge.tw/ShowProblem?problemid=k707)
- [o079. 4. 最佳選擇](https://zerojudge.tw/ShowProblem?problemid=o079)

# 題意分析
以一個3x3矩陣來說, 座標應該是這樣分布的

|(1,1)|(1,2)|(1,3)|
|---|---|---|
|(2,1)|(2,2)|(2,3)|
|(3,1)|(3,2)|(3,3)|

# 我的答案
### v1-1 WA 
- 正確答案是39133, 但我輸出0
- 未考慮取值的範圍並非從第一列開始的狀況

### v1-2 TLE 
- 修正未考慮取值的範圍並非從第一列開始的話, 會得到0的結果(因為提早結束循環了)

### v1-3 TLE
- 對每列測資都處理成前綴和, 仍不夠有效率

### v1-4 WA
- "*您共輸出 75250 行。*" (什麼情況????)
- 雙重前綴和，做成二維版的

### v1-5 AC(1.2s, 7.3MB)
- 有多筆測資，所以要無限循環，直到EOF為止

### v2-1 AC(0.6s, 10.2MB)
- 導入 itertools 的 accumulate
