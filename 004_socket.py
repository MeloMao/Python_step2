#!/usr/bin/python
#coding=utf-8
import socket

Host=raw_input("Please input the web's host name:")
IP = socket.gethostbyname(Host)
print("The web's IP is:"),
print(IP)