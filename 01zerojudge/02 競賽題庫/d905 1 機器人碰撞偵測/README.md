#

## 解題紀錄

### v1-1 NA(score: 84%)

- 初版

### v1-2 AC(20ms, 3.5MB)

- 修正判斷是否移動的邏輯

```diff
@@ 21,6 20,9 @@
- for i in bot_curr:
-     if 0 < bot_curr[i]['x'] <= n and 0 < bot_curr[i]['y'] <= n:
-         bot_curr[i]['x'] += direction[bot_curr[i]['d']][0]
-         bot_curr[i]['y'] += direction[bot_curr[i]['d']][1]
-     else:
-         bot_curr[i]['active'] = False
+ # 所有機器人同時移動
+ for i in bot_curr:
+     if bot_curr[i]['active']:
+         bot_curr[i]['x'] += direction[bot_curr[i]['d']][0]
+         bot_curr[i]['y'] += direction[bot_curr[i]['d']][1]
+         # 若下次移動會超出範圍，將 "active" 設置為 False
+         if ((not 0 < bot_curr[i]['x'] + direction[bot_curr[i]['d']][0] <= n) or 
+             (not 0 < bot_curr[i]['y'] + direction[bot_curr[i]['d']][1] <= n)):
+             bot_curr[i]['active'] = False
```


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
