#

## 解題紀錄

### v1-1 NA(score: 84%)

- 初版

### v1-2 AC(20ms, 3.5MB)

- 修正判斷是否移動的邏輯

### v1-3 AC(20ms, 3.5MB)

- 調整寫法，應該能讓可讀性好一些(吧?)

```diff
@@ -32,4 +32,1 @@
- temp = {i}
- for j in bot_prev:
-     if j not in temp and bot_curr[i]['x'] == bot_prev[j]['x'] and bot_curr[i]['y'] == bot_prev[j]['y']:
-         temp.add(j)
+ temp = {j for j in bot_prev if bot_curr[i]['x'] == bot_prev[j]['x'] and bot_curr[i]['y'] == bot_prev[j]['y']}
```
