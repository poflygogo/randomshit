## 解題思路

> 這題讓我一直在那邊吃葡萄吐葡萄皮，笑死

四種狀況:
1. 「過程中」只要曾發生過吐的比吃的多，輸出 "bu chi pu tao dao tu pu tao pi"
2. 「結算時」若吃的比吐的多，輸出 "chi pu tao bu tu pu tao pi"
3. 「結算時」若吃的和吐的一樣多，輸出 "chi pu tao tu pu tao pi"
4. 「結算時」若 1 和 2 同時發生，輸出 "chi pu tao bu tu pu tao pi, bu chi pu tao dao tu pu tao pi"

## 解題紀錄
### v1-1 AC(45ms, 6.5MB)

### v1-2 AC(41ms, 5.1MB)
- 移除一些非必要的變量與計算
  - 不再將資料轉成布林陣列
  - 不再將資料存到 data 變量中
  - 移除沒有用到的變量: flag_more_chi
