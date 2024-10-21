"""
-*- coding: utf-8 -*-
建立Python Script 擷取Data
main.py
"""

import requests
import pandas as pd


# 向伺服器發送 GET 請求
response = requests.get(r'http://localhost:8000')

# 確認請求成功
if response.status_code == 200:
    # 解析 json 數據
    data = response.json()

    # 轉換成 DataFrame
    customers = pd.DataFrame(data['customers'])

    # 將數據儲存到 Excel 檔案
    customers.to_excel(
        'customers_data.xlsx',
        index=False
    )
    print('數據已儲存到 customers_data.xlsx')
else:
    print(f'請求失敗，狀態碼: {response.status_code}')
