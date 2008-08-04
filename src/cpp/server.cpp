// based on the 'calculator' demo in the Thrift source

#include <concurrency/ThreadManager.h>
#include <concurrency/Mutex.h>
#include <concurrency/PosixThreadFactory.h>
#include <protocol/TBinaryProtocol.h>
//#include <server/TSimpleServer.h>
//#include <server/TThreadPoolServer.h>
#include <server/TThreadedServer.h>
//#include <server/TNonblockingServer.h>
#include <transport/TServerSocket.h>
#include <transport/TTransportUtils.h>

#include <iostream>
#include <stdexcept>
#include <sstream>

#include "../gen-cpp/Queue.h"

using namespace std;
using namespace facebook::thrift;
using namespace facebook::thrift::concurrency;
using namespace facebook::thrift::protocol;
using namespace facebook::thrift::transport;
using namespace facebook::thrift::server;

using namespace simplequeue;

using namespace boost;

#define PORT 9090

class QueueHandler : public QueueIf {
 public:
  QueueHandler() {}

  void ping() {
  }

  void push(const std::string& msg) {
    m_mutex.lock();
    m_queue.push_back(msg);
    m_mutex.unlock();
  }

  void pop(std::string& _return) {
    m_mutex.lock();
    if (m_queue.empty()) {
      m_mutex.unlock();
      _return = "";
      return;
    }
    _return = m_queue.front();
    m_queue.pop_front();
    m_mutex.unlock();
  }

protected:
  std::list<std::string> m_queue;
  Mutex m_mutex;

};

int main(int argc, char **argv) {

  shared_ptr<TProtocolFactory> protocolFactory(new TBinaryProtocolFactory());
  shared_ptr<QueueHandler> handler(new QueueHandler());
  shared_ptr<TProcessor> processor(new QueueProcessor(handler));
  shared_ptr<TServerTransport> serverTransport(new TServerSocket(PORT));
  shared_ptr<TTransportFactory> transportFactory(new TBufferedTransportFactory());

  /*TSimpleServer server(processor,
                       serverTransport,
                       transportFactory,
                       protocolFactory);*/


  /**
   * Or you could do one of these

  shared_ptr<ThreadManager> threadManager =
    ThreadManager::newSimpleThreadManager(workerCount);
  shared_ptr<PosixThreadFactory> threadFactory =
    shared_ptr<PosixThreadFactory>(new PosixThreadFactory());
  threadManager->threadFactory(threadFactory);
  threadManager->start();
  TThreadPoolServer server(processor,
                           serverTransport,
                           transportFactory,
                           protocolFactory,
                           threadManager);*/

  TThreadedServer server(processor,
                         serverTransport,
                         transportFactory,
                         protocolFactory);

  //TNonblockingServer server(processor, PORT);

  printf("Starting the server...\n");
  server.serve();
  printf("done.\n");
  return 0;
}
