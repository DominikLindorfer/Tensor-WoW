# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 19:12:37 2021

@author: dl
"""

from threading import Thread
from queue import Queue
import time


def slave(q):
    while True:
        signal = q.get()
        print(f"Got signal {signal}")
        if signal == "break":
            break
        time.sleep(0.01)
    print("Routine done")

def master(q,q1):
    q.put("signal1")
    time.sleep(0.2)
    q.put("signal2")
    time.sleep(0.2)
    q.put("break")
    
    q1.put("signal1 1")
    time.sleep(0.2)
    q1.put("signal2 1")
    time.sleep(0.2)
    q1.put("break")


def main():
    q = Queue()
    q1 = Queue()
    slavethread = Thread(target=slave, args=(q, ))
    slavethread1 = Thread(target=slave, args=(q1, ))
    masterthread = Thread(target=master, args=(q,q1, ))
    slavethread.start()
    slavethread1.start()
    masterthread.start()
    
    
main()