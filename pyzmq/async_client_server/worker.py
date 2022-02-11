import random
import sys
import zmq

port = "5555"
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f"tcp://localhost:{port}")
socket.subscribe(b"")

if sys.argv[1] == "1":
    pair_port = "5556"
    pair_socket = context.socket(zmq.PAIR)
    pair_socket.connect(f"tcp://localhost:{pair_port}")
    pair_socket.send(b"READY")


# Process 5 updates
while True:
    string = socket.recv_pyobj()
    print(string)
    if sys.argv[1] == "1":
        pair_socket.send_pyobj((random.uniform(0, 1)))
