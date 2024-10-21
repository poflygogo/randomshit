"""
-*- coding: utf-8 -*-
建立 Mock Server Data
server.py
需要執行時，就在 cmd 中執行 python -m http.server 或 python server.py
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):   # 注意是 do_GET 而非 do_get
        """設置回應標頭"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # 傳送一些簡單的數據(要符合 json 格式)
        data = {
            "customers": [
                {"id": "CUST1", "name": "王小明", "city": "台北市", "address": "中正區xx路"},
                {"id": "CUST2", "name": "李大華", "city": "高雄市", "address": "三民區xx路"},
                {"id": "CUST3", "name": "陳美麗", "city": "台中市", "address": "西屯區xx路"}
            ]
        }

        # 將數據轉換為 JSON 並傳送回應
        self.wfile.write(json.dumps(data).encode('utf-8'))


# 啟動 HTTP 伺服器
if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('伺服器正在運行...')
    httpd.serve_forever()
