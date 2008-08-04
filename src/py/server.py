#!/usr/bin/env python

# based on the 'calculator' demo in the Thrift source

import sys, os.path
sys.path.insert(0, os.path.join(os.path.abspath(os.path.split(sys.argv[0])[0]), '..', 'gen-py'))
import simplequeue.Queue
from simplequeue.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class QueueHandler:
    def __init__(self):
        self.queue = []

    def ping(self):
        return "pong"

    def push(self, obj):
        #print "push"
        self.queue.append(obj)

    def pop(self):
        if not len(self.queue): return ""
        return self.queue.pop(0)
      
handler = QueueHandler()
processor = simplequeue.Queue.Processor(handler)
transport = TSocket.TServerSocket(9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

#server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

# You could do one of these for a multithreaded server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
#server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

print 'Starting the server...'
server.serve()
print 'done.'
