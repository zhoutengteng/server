
# -*- coding:utf-8 -*-
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import json

class TestHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.protocal_version = "HTTP/1.1"
        self.send_response(200)
        self.send_header("Welcome", "Contect")
        self.end_headers()
        buf = get_data();
        print buf
        self.wfile.write(buf)

    def do_POST(self):
        length = self.headers.getheader('content-length');
        nbytes = int(length)
        data = self.rfile.read(nbytes)
        self.protocal_version = "HTTP/1.1"
        self.send_response(200)
        self.send_header("Welcome", "Contect")
        self.end_headers()
        self.wfile.write(data)
        save_data(data)

def get_data():
    f = open('redbag.txt', 'r')
    recordList = f.readlines()
    objectDict = {}
    for i in range(len(recordList)):
        oneline = recordList[i]
        if oneline.strip():

            key_value = json.loads(oneline.decode("unicode_escape"))
            objectDict[i] =  key_value
    return json.dumps(objectDict)

def save_data(data):
    print data
    f = open("redbag.txt", 'a+')
    f.write(data + '\n')
    f.close()

def start_server(port):
    ip = '127.0.0.1'
    http_server = HTTPServer((ip, int(port)), TestHTTPHandler)
    http_server.serve_forever() #设置一直监听并接收请求


if __name__ == '__main__' :
    start_server(8888)
