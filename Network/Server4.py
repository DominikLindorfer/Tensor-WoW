# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:07:41 2021

@author: dl
This actually Worked!!!
"""
import socket

server = socket.gethostbyname(socket.gethostname()) # 10.128.X.XXX which is the Internal IP
print(server)
port = 1701
clients = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))

s.listen(2)
print("Waiting for connection...")

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    conn.send(str.encode(f"{clients}"))
    clients += 1