## 解題紀錄

> 以下 NA(score:95%) 的解全部都是在 #2 吃了 MLE，故下面的結果會特別標示 #2 所占用的空間。

### v1-1 NA(score: 95%)(68.5MB)

- 初版，導入 `itertools.permutations`

### v1-2 NA(score: 95%)(68.4MB)

- 調整 `sort` 的時機，改使用 in-place 的做法

- 記憶體占用只少 0.1MB ，看來 `sort` 不是主要開銷

### v2-1 NA(score: 95%)(141MB)

- 使用 dfs 實現 permutations

- 記憶體占用變多了...

### v2-2 NA(score: 95%)(181.9MB)

- 修改 `seen` 保存的值，僅記錄元素的位置，而不保存數字

- 占用更多空間...

### v2-3 NA(score: 95%)(172.5MB)

- 不再將輸入的字串轉換成 int

- 也對，怎麼可能這樣就能解決呢

### v2-4 NA(score: 95%)(198.4MB)

- 導入內建模組 `array.array` 用更高效率的陣列取代 list

- 哭啊!!!!!

### v2-5 NA(score: 95%)(69.2MB)

- 試試看不再紀錄位置，而是回歸初衷，直接紀錄元素

- 這裡順便製作了 `testcase`，然後意識到真正的性能開銷可能是出現在 `seen`

### v2-6 NA(score: 95%)(69.2MB)

- 修改 `seen` 保存資料的方式，用 flag 標記每個元素是否有被使用過

### v2-7 NA(score: 95%)(67.8MB)

- 調整輸出方式，導入 `sys.stdout` 處理輸出

### v2-8 AC(4.5s, 35.5MB)

- 不再維護 `seen`，而是直接檢查元素是否有在 `path` 出現過

### v2-9 AC(3.7s, 35.5MB)

- 調整 `path` 紀錄元素的方式，使用 dict[int, int] 的格式紀錄順序

- 維護一個 `depth` 變量紀錄深度，避免頻繁調用 `len()`
