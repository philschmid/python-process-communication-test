from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import time
import zmq
import uvicorn

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

for i in range(4):
    subprocess.Popen(["python3", "worker.py", str(i)])


client_conntected = False
while not client_conntected:
    print("Waiting for clients to connect")
    response = pair_socket.recv()
    if response.decode() == "READY":
        client_conntected = True
        print("clients connected")


async def test(request):
    body = await request.json()
    print(f"sending {body['inputs']}")
    socket.send_pyobj(body["inputs"])
    print("waiting for response")
    response = pair_socket.recv_pyobj()
    print("response:", response)
    return JSONResponse({"score": response})


app = Starlette(
    debug=False,
    routes=[
        Route("/", test, methods=["POST"]),
    ],
)

uvicorn.run(app, host="0.0.0.0", port=8500, log_level="info", workers=1)
