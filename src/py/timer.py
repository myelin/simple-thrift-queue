#!/usr/bin/env python

# based on the 'calculator' demo in the Thrift source

from client import connect, Thrift
import time

try:
  (transport, client) = connect()

  n = 2000

  print "timing ping()"
  start = time.time()
  for i in range(n):
    client.ping()
  t = (time.time() - start); print t, n / t

  print "timing push()"
  start = time.time()
  for i in range(n):
    client.push(str(i))
  t = (time.time() - start); print t, n / t

  print "timing pop()"
  start = time.time()
  while 1:
    if not client.pop(): break
  t = (time.time() - start); print t, n / t
  
  transport.close()

except Thrift.TException, tx:
  print 'exception: %s' % (tx.message)
