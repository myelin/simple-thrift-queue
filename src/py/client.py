#!/usr/bin/env python

# based on the 'calculator' demo in the Thrift source

import sys, os.path
sys.path.insert(0, os.path.join(os.path.abspath(os.path.split(sys.argv[0])[0]), '..', 'gen-py'))
import simplequeue.Queue
from simplequeue.ttypes import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def connect():
  transport = TSocket.TSocket('localhost', 9090)
  transport = TTransport.TBufferedTransport(transport)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = simplequeue.Queue.Client(protocol)
  transport.open()
  return (transport, client)
