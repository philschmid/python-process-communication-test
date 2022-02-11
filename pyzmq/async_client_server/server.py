import subprocess
import zmq
import random
import sys
import time

# port = "5555"

# context = zmq.Context()
# socket = context.socket(zmq.PUB)
# socket.bind(f"tcp://*:{port}")


# while True:
#     topic = "req"
#     message = "Hello"
#     print(f"topic:{topic} message:{message}")
#     socket.send(bytes(f"{topic} {message}", "utf-8"))
#     time.sleep(2)

import zmq
import random
import sys
import time

port = "5555"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(f"tcp://*:{port}")

server_port = "5556"
pair_socket = context.socket(zmq.PAIR)
pair_socket.bind(f"tcp://*:{server_port}")

# while True:
topic = "deepspeed"
message = "Hello"

for i in range(4):
    subprocess.Popen(["python3", "worker.py", str(i)])


client_conntected = False
while not client_conntected:
    print("Waiting for clients to connect")
    response = pair_socket.recv()
    if response.decode() == "READY":
        client_conntected = True
        print("clients connected")


print(f"sending topic:{topic} message:{message}")
socket.send(bytes(f"{topic} {message}", "utf-8"))
print("waiting for response")
response = pair_socket.recv()
print("response:", response)
