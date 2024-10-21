[官方文檔](https://pandas.pydata.org/docs/user_guide/index.html)

此處僅作為個人筆記使用

# [Class] 創建 DataFrame 對象
pandas 使用其特色的 DataFrame 處理二維表格數據。

DataFrame 是一種二維化的標籤陣列。

```py
import pandas

data = [
    'Product Name': ['Widget A', 'Widget B', 'Widget C', 'Widget D'],
    'Sale Price': [25.50, 15.75, 30.00, 10.00],
    'Quantity Sold': [100, 200, 150, 300]
]
df = pandas.DataFrame(data)
```

## [方法] `to_excel` : 將 DataFrame 保存到 Excel 文件中
```py
import pandas
df = pandas.DataFrame()
df.to_excel('example.xlsx', index=False)
```