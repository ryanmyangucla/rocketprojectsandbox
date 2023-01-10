import socket
import time
import random

HOST = "127.0.0.1"
PORT = 5000

i = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Waiting for client to connect")
        print(f"Connected by {addr}")
        while True:
            sleepTime = 0.01 * random.randint(5, 10)
            time.sleep(sleepTime)
            data = []
            data.append(str(i))
            i += sleepTime
            for _ in range(4):
                data.append(str(random.randint(-10, 10)))
            
            print((','.join(data) + '\n').encode('utf-8'))
            conn.sendall((','.join(data) + '\n').encode('utf-8'))