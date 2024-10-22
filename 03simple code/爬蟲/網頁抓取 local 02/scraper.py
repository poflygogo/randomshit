# save this as scraper.py

import requests
from bs4 import BeautifulSoup


# 發送 GET 請求到伺服器
url = 'http://localhost:8080/index.html'
response = requests.get(url)

# 確保請求成功
if response.status_code == 200:
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到 hi 標籤
    h1_tag = soup.find('h1')

    # 顯示 hi 的內容
    if h1_tag:
        print(f'Found H1 Title: {h1_tag.text}')

    else:
        print('H1 tag not found')

else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
