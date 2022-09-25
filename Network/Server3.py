# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:32:14 2021

@author: dl
"""

import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 8080))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data
        print(from_client)
        conn.send("I am SERVER<br>")
    conn.close()
    print('client disconnected')