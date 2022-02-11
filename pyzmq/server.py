# import subprocess


# for i in range(2):
#     subprocess.Popen(["python3", "inference.py"])

# #
# #   Hello World server in Python
# #   Binds REP socket to tcp://*:5555
# #   Expects b"Hello" from client, replies with b"World"
# #

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

clients_ready = False

for i in range(10):
    #  Wait for next request from client
    if not clients_ready:
        print("waiting for clients to be ready")
        message = socket.recv()
        if message.decode() == "READY":
            print("clients are ready")
            clients_ready = True
    else:
        #  Send reply back to client
        socket.send(b"World")
        score = socket.recv()
        print(f"Received score: {score}")
socket.close()
print(socket.closed)
