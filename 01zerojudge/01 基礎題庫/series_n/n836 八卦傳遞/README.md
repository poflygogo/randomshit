#

## 解題紀錄

### v1-1 AC(0.7s, 4.9MB)

- 初版

### v1-2 AC(0.5s, 4.8MB)

- 簡單調整一下 `find`，確保路徑能好好的壓縮起來

```diff
@@ -13,2 +13,2 @@
- idx = find(arr[x])
- return arr[idx]
+ arr[x] = find(arr[x])
+ return arr[x]
```

### v1-3 AC(0.5s, 4.9MB)

- 再壓，確保 `union` 時永遠都是比較小的樹合併到大的

```diff
@@ +8,1 @@
+ size = [1] * (n + 1)

@@ -20,2 +22,4 @@
-    if x_root != y_root:
-        arr[y_root] = x_root
+    if x_root != y_root:
+        if size[x_root] < size[y_root]:
+            x_root, y_root = y_root, x_root
+        arr[y_root] = x_root
+        size[x_root] += size[y_root]
```

其他人到底是用什麼方式做到用更多的記憶體換執行效率的呢...
