from multiprocessing.connection import Listener

listener = Listener(("localhost", 6000), authkey=b"secret password")
running = True
while running:
    conn = listener.accept()
    print("connection accepted from", listener.last_accepted)
    while True:
        msg = conn.recv()
        print(type(msg))
        print(msg["inputs"])

        if msg == "close connection":
            conn.close()
            break
        if msg == "close server":
            conn.close()
            running = False
            break
listener.close()
