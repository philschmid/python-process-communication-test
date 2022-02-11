from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import time
import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

clients_ready = False


async def test(request):
    body = await request.json()
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
    start_time = time.time()
    score = 1
    return JSONResponse({"score": score})


app = Starlette(
    debug=False,
    routes=[
        Route("/", test, methods=["POST"]),
    ],
)
