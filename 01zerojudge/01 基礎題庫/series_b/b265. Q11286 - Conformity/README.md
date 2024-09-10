我想到的 3 個做法
1. 不導入任何模組，使用字典 dict 統計每個元素出現的頻率
2. 導入 itertools 的 groupy
3. 導入 collections 的 Counter

## 解題紀錄
### v1-1 AC(0.4s, 16.8MB)
- [說明](https://gist.github.com/poflygogo/892fece837275218dea0da097a2d23af)

### v2-1 AC(0.4s, 35.1MB)
- 導入 itertools 的 groupby
> 占用的空間更多了......

### v2-2 AC(0.3s, 4.6MB)
- 調整紀錄資料的格式
> 效率好太多了吧!?

### v1-2 AC(0.4s, 11.6MB)
- 調整紀錄資料的格式
> 所以字串並非總是代表不好 hmm

### v3-1 AC(0.6s, 9.7MB)
- 導入 collections 的 Counter

### v3-2 AC(0.2s, 9.2MB)
- 調整建立 Counter 對象的方式，不再頻繁的調用 update
> Counter 威武阿!!!