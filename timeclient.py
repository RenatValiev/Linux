#!/usr/bin/python3

import socket

HOST = input("Введите IP-адрес сервера: ")
PORT = 1303

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)

print('Полученное время:', data.decode())
