## 類題
- [a291. nAnB problem](https://zerojudge.tw/ShowProblem?problemid=a291) | [zerojudge](https://zerojudge.tw/)
- [c276. 沒有手機的下課時間](https://zerojudge.tw/ShowProblem?problemid=c276) | [zerojudge](https://zerojudge.tw/)


## 解題紀錄
### v0.1
- 測試時出現錯誤答案，因為沒有考慮到重複計算的部分(如果A和B有重複的數字時，不會排除A)
- 因為還沒正式上場前就在測試時失敗，所以是v0.1

### v1 RE
- 讀取到錯誤的資料(應該讀取到test次數，但卻讀取到了一個test內容)
- 修正B的值沒有被正確計算的問題
- 處理軟複製一個物件後，會連帶影響所有相關物件，導致原始數據丟失(說人話就是只能test一次, 第2次會出bug)

### v2 TLE
- 修正當讀取到空白數據時，會導致無法按照理想順序輸入數據的問題

### v3 WA(應輸出1A1B，實際輸出1A2B)
- 導入sys的stdin，希望這能提高一點效率
- 未考慮到當B出現重複值時的狀況

### v4 AC(2.4s, 18.7MB)
- 修正當B有重複值時，會重複計算的狀況。(其實也就添加一行)
