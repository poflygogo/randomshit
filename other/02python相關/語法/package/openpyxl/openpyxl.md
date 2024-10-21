[openpyxl 官方文檔](https://openpyxl.readthedocs.io/en/stable/tutorial.html#)

此處僅作為個人筆記使用

# `Workbook()` 創建新的 excel 工作簿
```py
import openpyxl
wb = openpyxl.Workbook()
```

## [屬性] `active`: 工作表
每一個工作簿都會自動啟用一個工作表，調用 active 可以調用當前活躍的工作表的屬性
```py
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
```

其實也可以透過傳入 offset 獲取指定的工作表，語法是 `workbook.worksheets[index]` ，每個工作表在工作簿中都有對應的索引，從 0 開始。例如 `workbook.worksheets[0]` 就是第一個工作表。

如果知道工作表的名稱，也可以使用 key 獲取指定名稱的工作表，語法是 `workbook[sheet_name]`，如 `workbook['Data']` 意思是獲取一個名為 Data 的工作表。

[方法] `create_sheet`: 新增工作表

總是會有需要新增工作表的時候，這時候就可以對 `Workbook` 對象使用 `create_sheet` 方法，語法是 `workbook.create_sheet(title='New Sheet')`，title 傳入工作表的名稱。

[方法] `remove` 移除工作表

[方法] `copy` 複製工作表

### [屬性] `title`: 修改工作表的名稱
預設值是 sheet0

### 寫入數據、修改儲存格

#### 透過 key 修改指定儲存格的內容
可以透過傳入 key 修改指定位置的儲存格，就像 dict 一樣。

key 的格式為 `字母 + 數字` ，例如 `['A1']` 代表位於第 1 行第 1 列的儲存格，需要注意 key 是一個字串 string

```py
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = 'Name'
sheet['B1'] = 'Age'
```

#### [方法] `append`: 批量修改一整列(row)的數據
```py
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = 'Name'
sheet['B1'] = 'Age'

sheet.append(['Alice', 25])
sheet.append(['Bob', 30])
sheet.append(['Charlie', 35])
```

### 修改儲存格樣式
透過 `openpyxl.styles.Font()` 修改儲存格的樣式

```py
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'].font = openpyxl.styles.Font(bold=True)
```

## [方法] `save`: 儲存 Excel 文件
對 `Workbook` 對象使用 `save` 方法可以儲存文件，若問件不存在，則創建一份新的文件。

```py
import openpyxl
wb = openpyxl.Workbook()

wb.save('test.xlsx')
```