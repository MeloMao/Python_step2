#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket               # 导入 socket 模块

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口
s.bind((host, port))        # 绑定端口

s.listen(5)                 # 等待客户端连接
while True:
    c, addr = s.accept()     # 建立客户端连接。
    print 'connect：', addr
    c.send("welcome to melo's world!")
    c.close()