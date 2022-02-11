from multiprocessing.connection import Client
import time

# Client 1
conn = Client(("localhost", 6000), authkey=b"secret password")

while True:
    time.sleep(2)
conn.send("close connection")
conn.close()
