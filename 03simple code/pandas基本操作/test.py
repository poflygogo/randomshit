# -*-coding: utf-8-*-
# python 3.12
# pandas 2.2.3

import pandas as pd

# 讀取顧客基本資料和地址資料
customer_df = pd.read_excel('Customer_basic_info.xlsx')
address_df = pd.read_excel('customer_address_info.xlsx')

# 檢查是否有缺少「縣市」、「鄉鎮區」或「地址」的欄位
missing_address = address_df[
    address_df[['縣市', '鄉鎮區', '地址']].isnull().any(axis=1) |
    (address_df[['縣市', '鄉鎮區', '地址']].map(lambda x: str(x).strip()) == '').any(axis=1)
    ]

# 如果有缺少地址的顧客，將結果輸出到 missing_address.xlsx 並進行通知
if not missing_address.empty:
    missing_customer_info = pd.merge(
        missing_address[['顧客ID']], customer_df,
        on='顧客ID',
        how='left'
    )
    missing_customer_info.to_excel(
        'missing_address.xlsx',
        index=False,
    )
    print('有缺少地址的顧客，詳細內容請見 missing_address.xlsx')

# 將「縣市」、「鄉鎮區」、「地址」欄位合併成「完整地址」
address_df['完整地址'] = (
        address_df['縣市'].fillna('') +
        address_df['鄉鎮區'].fillna('') +
        address_df['地址'].fillna('')
)

# 合併顧客基本資料和地址資料，根據顧客ID匹配
merge_df = pd.merge(
    customer_df,
    address_df[['顧客ID', '完整地址']],
    on='顧客ID',
    how='left'
)


# 根據顧客生日將其分配到不同季度
def assign_quarter(birthday):
    month = birthday.month
    if month in (1, 2, 3):
        return 'Q1'
    elif month in (4, 5, 6):
        return 'Q2'
    elif month in (7, 8, 9):
        return 'Q3'
    else:
        return 'Q4'


# 將生日轉換為日期格式並劃分季度
merge_df['Quarter'] = pd.to_datetime(merge_df['生日']).apply(assign_quarter)


# 將顧客資料按照季度分開存到不同的工作表
with pd.ExcelWriter('customer_summary.xlsx', engine='openpyxl') as writer:
    for quarter in ('Q1', 'Q2', 'Q3', 'Q4'):
        quarter_df = merge_df[merge_df['Quarter'] == quarter]
        if not quarter_df.empty:
            quarter_df.to_excel(
                writer,
                sheet_name=quarter,
                index=False
            )
