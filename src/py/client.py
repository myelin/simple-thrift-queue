#!/usr/bin/env python

import sys, os.path, time
sys.path.insert(0, os.path.join(os.path.abspath(os.path.split(sys.argv[0])[0]), '..', 'gen-py'))
import simplequeue.Queue
from simplequeue.ttypes import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:

  # Make socket
  transport = TSocket.TSocket('localhost', 9090)

  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)

  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  # Create a client to use the protocol encoder
  client = simplequeue.Queue.Client(protocol)

  # Connect!
  transport.open()

  client.ping()
  print 'ping()'

  start = time.time()
  n = 10000
  for i in range(n):
      client.push(str(i))
  print n / (time.time() - start)

  while 1:
      client.pop()

  # Close!
  transport.close()

except Thrift.TException, tx:
  print 'exception: %s' % (tx.message)
