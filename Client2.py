# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:25:14 2021

@author: dl
"""

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('140.78.103.45', 10000)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    
    # Send data
    message = 'This is the message.  It will be repeated.'
    print(sys.stderr, 'sending "%s"' % message)
    sock.sendall(message.encode('utf-8'))

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    # while amount_received < amount_expected:
    #     data = sock.recv(16)
    #     amount_received += len(data)
    #     print (sys.stderr, 'received "%s"' % data)

finally:
    print(sys.stderr, 'closing socket')
    sock.close()