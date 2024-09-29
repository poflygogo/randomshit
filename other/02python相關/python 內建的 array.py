"""
創建 array 時, 需要指定一個型態碼(typecode)來表示元素的資料型態。常用的型態碼有:
'b': 有符號的char (布林值在這)
'B': 無符號的 char
'u': Unicode character
'i': 有符號的 int
'I': 無符號的 int
'f': float
"""


from array import array


# 建立新 array
my_array = array('i', [1, 2, 3, 4, 5, 6, 7, 8])

# 在末端添加元素
my_array.append(9)

# 在指定位置插入新元素
my_array.insert(0, 0)

# 批量在末端添加元素
my_array.extend([10, 11, 12, 13])

# 修改指定位置的元素
my_array[6] = 100

# 將指定位置的元素取出後刪除
num = my_array.pop(5)

# 移除指定元素
my_array.remove(10)

# 計算指定元素出現的頻率
my_array.count(4)

# 反轉元素排列順序
my_array.reverse()

# 沒有 sort() 方法
# my_array.sort()

# 尋找指定元素的位置
my_array.index(3)

# 沒有 clear
# my_array.clear()

# 計算 array 的元素數量
length = len(my_array)
print(length)

"""
其他
"""
# 印出當前記憶體位置與array的元素數量
info = my_array.buffer_info()

# 不知道幹嘛的，但調用兩次會得到原數據
my_array.byteswap()

# 讀取一個文件對象的內容，並轉換成 array
my_array.fromfile()

# 將所有元素寫入到文件對象
my_array.tofile()

my_array.frombytes()

my_array.fromunicode()

# 把 array 轉換成 list
my_array.tolist()