#!/usr/bin/env python

from client import connect, Thrift
import time

transport, client = connect()

n = 0
start = time.time()
while 1:
    for i in range(1000):
        n += 1
        client.push("testing #%d" % n)
    print n, n / (time.time() - start)
