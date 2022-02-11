#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import random
import zmq
import time
import sys


print(sys.argv[1])

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
socket.send(b"READY")
while True:
    print(socket.closed)
    #  Get the reply.
    message = socket.recv()
    print(message)
    if sys.argv[1] == "1":
        socket.send(bytes(str(random.uniform(0, 1)), "utf-8"))
    else:
        socket.send(b"EMPTY")
    time.sleep(1)
