## 解題思路

等差數列和公式為 $ S_n = \frac{(a_1 + a_n) \times n}{2} $

所以只需要算出等差數列和後，再減掉 list 中所有元素的和，即是缺少的數字

## 解題紀錄
### v1-1 AC(48ms, 3.3MB)

### v1-2 AC(38ms, 3.3MB) 
- 找到重複值時，使用 break 提早結束 for 循環

### v1-3 AC(33ms, 3.3MB)
- 不再 sort
- 使用列表生成式，而非 map

### v1-4 AC(32ms, 3.6MB)
- 導入 sys.stdin
