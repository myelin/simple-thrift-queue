#!/usr/bin/env python

from client import connect, Thrift
import time

transport, client = connect()

n = 0
while 1:
    msg = client.pop()
    if msg:
        n += 1
        if not (n % 100):
            print msg
    else:
        time.sleep(0.1)
