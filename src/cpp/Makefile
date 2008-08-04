THRIFT_DIR = /usr/local/include/thrift
LIB_DIR = /usr/local/lib

GEN_SRC = ../gen-cpp/queue_types.cpp ../gen-cpp/Queue.cpp

default: server #client

server: server.cpp
	g++ -o server -I${THRIFT_DIR}  -I../gen-cpp -L${LIB_DIR} -lthrift -lthriftnb -levent server.cpp ${GEN_SRC}

#client: CppClient.cpp
#	g++ -o CppClient -I${THRIFT_DIR}  -I../gen-cpp -L${LIB_DIR} -lthrift CppClient.cpp ${GEN_SRC}

clean:
	$(RM) -r CppClient CppServer

run: server
	env LD_LIBRARY_PATH=/usr/local/lib ./server
