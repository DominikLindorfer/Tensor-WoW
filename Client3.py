# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:32:30 2021

@author: dl
"""

#!/usr/bin/env python3

import socket

HOST = '185.237.96.43'  # The server's hostname or IP address
PORT = 6002        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
