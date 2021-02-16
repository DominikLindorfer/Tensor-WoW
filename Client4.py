# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:12:20 2021

@author: dl
This actually Worked!!!
"""
import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "45.83.41.211"
        self.port = 1701
        self.addr = (self.server, self.port)
        self.id = int(self.connect())

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

network = Network()
print(f"Connected as client {network.id}")
