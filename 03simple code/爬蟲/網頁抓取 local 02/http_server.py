# -*- coding: utf-8 -*-
# save this as http_server.py

import http.server
import socketserver


# 設定伺服器的端口
PORT = 8080

# 設定處理的 Handler 使用 HTTP Server
Handler = http.server.SimpleHTTPRequestHandler

# 啟動伺服器，並提供 index.html
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print(f'Serving at port {PORT}')
    httpd.serve_forever()
