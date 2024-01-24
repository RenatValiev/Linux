import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 1303

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            now = datetime.now().strftime("%d.%m.%Y %H:%M")
            conn.sendall(now.encode())