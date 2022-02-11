import zmq
import time
import sys


print(sys.argv)

# context = zmq.Context()

# #  Socket to talk to server
# print("Connecting to hello world server…")
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:5555")


# while True:
#     #  Wait for next request from client
#     message = socket.recv()
#     print(message)
#     print(socket.closed())
#     #  Send reply back to client
#     socket.send(b"score 1")
