#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import http.server
import socketserver
import os
from urllib.parse import unquote

PORT = 8080

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # เพิ่ม headers สำหรับ CORS และ download
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        
        # ถ้าเป็นไฟล์ .apk ให้ดาวน์โหลด
        if self.path.endswith('.apk'):
            self.send_header('Content-Type', 'application/vnd.android.package-archive')
            self.send_header('Content-Disposition', 'attachment; filename="Meetang88.apk"')
        
        http.server.SimpleHTTPRequestHandler.end_headers(self)
    
    def do_OPTIONS(self):
        # รองรับ CORS preflight requests
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
    
    def do_POST(self):
        # รองรับ POST requests (ส่งกลับ 200 OK)
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"status": "ok"}')
    
    def do_GET(self):
        # แปลง URL path
        if self.path == '/':
            self.path = '/index.html'
        elif self.path == '/download':
            self.path = '/index.html'
        elif self.path == '/install':
            self.path = '/install.html'
        elif self.path == '/download-apk':
            self.path = '/Meetang88.apk'
        
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🚀 Server กำลังทำงานที่ http://localhost:{PORT}")
        print(f"📱 หน้าดาวน์โหลด: http://localhost:{PORT}/")
        print(f"📦 ไฟล์ APK: http://localhost:{PORT}/Meetang88.apk")
        print("กด Ctrl+C เพื่อหยุด server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✅ Server หยุดทำงานแล้ว")

